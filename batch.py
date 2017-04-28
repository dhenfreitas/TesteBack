import random
from random import randint
import string
import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect("database.db")
 
cursor = conn.cursor()

N = input("Qual o tamanho de N? ")

N = int(N)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


try:
	cursor.execute("""CREATE TABLE tb_customer_account
                  (id_customer,
				   cpf_cnpj,
				   nm_customer,
				   is_active,
				   vl_total,
				   PRIMARY KEY ( id_customer )) 
               """)

	actualSize = 1
			   
except OperationalError: 
    cursor.execute("select count(*) from tb_customer_account")

actualSize = cursor.fetchone()[0]
actualSize += 1
customers = [(actualSize, randint(00000000000,99999999999), id_generator(8, "abcdefghijklmnopqrstuyvxwz") + " " + id_generator(8, "abcdefghijklmnopqrstuyvxwz"), randint(0,1), randint(0,1000))]
print(actualSize)

for x in range(actualSize, N):
	temp = [(x, randint(00000000000,99999999999), id_generator(8, "abcdefghijklmnopqrstuyvxwz") + " " + id_generator(8, "abcdefghijklmnopqrstuyvxwz"), randint(0,1), randint(0,1000))]
	customers.extend(temp)
	
cursor.executemany("INSERT INTO tb_customer_account VALUES (?,?,?,?,?)", customers)
conn.commit()

for row in cursor.execute('SELECT nm_customer FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700 ORDER BY vl_total DESC'):
        print(row)

print('Média')
for mean in cursor.execute('SELECT AVG(vl_total) FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700 ORDER BY vl_total DESC'):
        print(mean)
		
cursor.close()
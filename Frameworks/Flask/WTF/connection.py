import mysql.connector

host='localhost'
database='testdb'
username='root'
password=' '

query="INSERT INTO 'user' ('firt_name','last_name','email') VALUES('rob','stark','rob@gmail.com')"

try:
	connection=mysql.connector.connect(host=host,database=database,user=username,password=password)
	cursor=connection.cursor()
	cursor.execute(query)

except:
	print("connection Failed !")
finally:
	if connection.is_connect():
		connection.close()



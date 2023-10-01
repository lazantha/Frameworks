import mysql.connector
query="CREATE TABLE login (log_id INT PRIMARY KEY AUTO_INCREMENT , name VARCHAR(20),email VARCHAR(20),password VARCHAR(20))";
try:
	connection=myslq.connector.connect(host='localhost',database='medical_db',user='root',password=None)
	cursor=connection.cursor()
	cursor.execute(query)
except:
	print("Conection Failed !")
finally:

	if connection.is_connected():
		connection.close()

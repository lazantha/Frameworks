# Sucess !
import mysql.connector

class MySql:
	host=''
	database=''
	user=''
	connection=''
	password=''
	connection=mysql.connector.connect(host=host,database=database,user=user,password=None)
	def __init__(self,host,databse,user,password):
		self.host=host
		self.database=database
		self.user=user
		self.password=password

	#for insertions
	def table(self,query,data):
		try:
			connection=None
			connection=self.connection
			cursor=connection.cursor(prepared=True)
			cursor.execute(query,data)
			connection.commit()
			print("Success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")
	
	def insertData(self,query):
		try:
			connection=None
			connection=self.connection
			cursor=connection.cursor(prepared=True)
			cursor.execute(query)
			connection.commit()
			print("Success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")
	
	# For parameter Binding and foreing keys
	#use comma after created tuple when binding arguments if it has One Argument 
	def fetchOneForeing(self,query,data):
		try:
			connection=None
			connection=self.connection
			cursor=connection.cursor(prepared=True)
			cursor.execute(query,data)
			result=cursor.fetchone()
			return(result[0])
			print("getting success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")

	#For multiple foreing keys data bind
	def fetchAllMulForeing(self,query,data):
		try:
			connection=None
			connection=connection
			cursor.execute(query,data)
			result=cursor.fetchall()
			return(result)
			print("getting success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")



		

	# FOR SINGLE QUERY
	def fetchOne(self,query):
		try:
			connection=None
			connection=connection
			cursor.execute(query)
			result=cursor.fetchone()
			return result[0]
			print("getting success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")
	


	#FOR SINGLE QUERY WITHOUT BINDING 
	def fetchMultiVal(self, query):


		    connection = None  # Define connection outside the try block
		    try:
		        connection =connection
		        cursor = connection.cursor(prepared=True)
		        cursor.execute(query)
		        result = cursor.fetchall()
		        print("getting success !")  # Move this line before the return statement
		        return result
		    except mysql.connector.Error as error:
		        print("query failed {}".format(error))
		    finally:
		        if connection is not None and connection.is_connected():
		            connection.close()
		            print("Connection Closed !")


	
	#without binding
	def delete(self, query, host, database, user):

		try:
			connection = None
			connection = connection
			cursor = connection.cursor(prepared=True)
			cursor.execute(query)
			connection.commit()  # Commit the deletion operation
			print("Deletion successful!")
		except mysql.connector.Error as error:
			print("Query failed: {}".format(error))
		finally:
			if connection is not None and connection.is_connected():
				cursor.close()  # Close the cursor
				connection.close()  # Close the connection
				print("Connection closed!")

	
	def deleteMulti(self,query,data,host,database,user):
		try:
			connection=None
			connection=connection
			cursor.execute(query)
			print("Success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if connection != None and connection.is_connected():
				connection.close()
				print("Connection Closed !")

	

	








	









 



# newSql=MySql()
# query="INSERT INTO user VALUES(2,'nimal','nimalPass');"
# newSql.table(query,host,database,user,password)

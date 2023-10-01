import mysql.connector
class Mysql:
	def __init__(self):
		self.host='localhost'
		self.database='test_medical_db'
		self.user='root'
		self.password=None
		self.connection=mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)
		self.cursor=self.connection.cursor(prepared=True)



	def fetchOneForeing(self,query, data):
		try:
			self.cursor.execute(query,data)
			result=self.cursor.fetchone()
			if result:
				return (result)
			else:
				return "no values"
		except mysql.connector.Error as error:
			print("Query Failed {}".format(error))
		finally:
			if self.connection != None and self.connection.is_connected():
				self.connection.close()
				print("Coneection CLosed !")



	def getMain(self,department):
		try:
			query="SELECT st.email,first_name,id_card,mi.medical_sheet FROM students AS st INNER JOIN medical_infor AS mi ON st.user_id =mi.user_id INNER JOIN departments AS dep ON st.department_id=dep.id WHERE dep.calling_name=%s ORDER BY mi.recorded_time DESC;"
			self.cursor.execute(query,(department,))
			result=self.cursor.fetchall()
			if result:
				return (result)
			else:
				return "no values"
		except mysql.connector.Error as error:
			print("Query Failed {}".format(error))
		finally:
			if self.connection != None and self.connection.is_connected():
				self.connection.close()
				print("Coneection CLosed !")


	def fetchAllMulForeing(self,query):
		try:
			self.cursor.execute(query)
			result=self.cursor.fetchall()
			return(result)
			print("getting success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if self.connection != None and self.connection.is_connected():
				self.connection.close()
				print("Connection Closed !")

	def fetchAllMulForeingAll(self,query,data):
		try:
			self.cursor.execute(query,data)
			result=self.cursor.fetchall()
			return(result)
			print("getting success !")
		except mysql.connector.Error as error:
			print("query failed {}".format(error))
		finally:
			if self.connection != None and self.connection.is_connected():
				self.connection.close()
				print("Connection Closed !")




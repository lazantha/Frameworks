class Binary:
	def convertToBinary(self,filename):
		with open(filename,'rb')as file:
			binary_data=file.read()
			return binary_data

	def ConvertToFile(self,binary_data,filename):
		with open(filename,'wb')as file:
			file=file.write(binary_data)
			return file



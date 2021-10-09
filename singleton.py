database = {
	"mexico" : ["64382", "62819", "69312"],
	"usa" : ["12343", "12355", "12346"],
	"canada" : ["35921", "32354", "32346","14380"]
}

class ZipCodes():
	def get_data(country):
		return database[country]

class ZipCodesSingleton(ZipCodes):
	
	__instance = None
	
	@staticmethod
	def get_instance():
		if ZipCodesSingleton.__instance == None:
			ZipCodesSingleton()
		return ZipCodesSingleton.__instance

	def __init__(self):
		if ZipCodesSingleton.__instance != None:
			raise Exception("Singleton cannot de instantied more than once!")
		else:
			ZipCodesSingleton.__instance = self

	@staticmethod
	def get_data(country):
		print(database[country])

z = ZipCodesSingleton()
print(z)
z.get_data("mexico")

z2 = ZipCodesSingleton.get_instance()
print(z2)
z2.get_data("canada")


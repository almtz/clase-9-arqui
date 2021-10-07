from abs import ABCMenta, abstractstaticmethod

database = {
	"mexico" : ["64382", "62819", "69312"],
	"usa" : ["12343", "12355", "12346"],
	"canada" : ["35921", "32354", "32346","14380"]
}

class ZipCodes():
	def get_data(country):
		print(database[country])

class ZipCodesSingleton():
	
	__instance = None
	
	@staticmethod
	def get_instance():
		if ZipCodesSingleton.__instance == None:
			ZipCodesSingleton()
			return __instance

	def __init__(self, zipcode):
		if ZipCodesSingleton.__instance != None:
			rise Exception("Singleton cannot de instantied more than once!")
		else:
			self.zipcode = zipcode
			ZipCodesSingleton.__instance = self

	@staticmethod
	def print_data():
		print("Name: {ZipCodesSingleton.__instance.zipcode}")
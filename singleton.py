from abc import ABCMeta, abstractstaticmethod

class IZipCodes(metaclass=ABCMeta):
	@abstractstaticmethod
	def get_data():
		""" Interface Method """

class ZipCodesSingleton(IZipCodes):
	
	__instance = None
	__database = {
	"mexico" : ["64382", "62819", "69312"],
	"usa" : ["12343", "12355", "12346"],
	"canada" : ["35921", "32354", "32346","14380"]
}
	
	@staticmethod
	def get_instance():
		if ZipCodesSingleton.__instance == None:
			ZipCodesSingleton()
		else:
			print("Singleton cannot de instantied more than once!")
		return ZipCodesSingleton.__instance

	def __init__(self):
		if ZipCodesSingleton.__instance == None:
			ZipCodesSingleton.__instance = self
		

	def delete(self):
		print("Instance deleted" )
		ZipCodesSingleton.__instance = None


	@staticmethod
	def get_data(country):
		print(ZipCodesSingleton.__database[country])

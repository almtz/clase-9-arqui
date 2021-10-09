from abc import ABCMeta, abstractstaticmethod
database = {
	"mexico" : ["64382", "62819", "69312"],
	"usa" : ["12343", "12355", "12346"],
	"canada" : ["35921", "32354", "32346","14380"]
}

class IZipCodes(metaclass=ABCMeta):
	@abstractstaticmethod
	def get_data():
		""" Interface Method """
		
class ZipCodes(IZipCodes):
	def get_data(self, country):
		return database[country]

class ProxyZipCodes(IZipCodes):
	def __init__(self):
		self.zipCodes = ZipCodes()
	
	def get_data(self, country):
		print(self.zipCodes.get_data(country))

z = ZipCodes()
print(z.get_data("usa"))

z2 = ProxyZipCodes()
z2.get_data("mexico")

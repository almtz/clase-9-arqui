from abc import ABCMeta, abstractstaticmethod
from singleton import ZipCodesSingleton

class ProxyZipCodes():
	def __init__(self):
		self.zipCodes = ZipCodesSingleton.get_instance()
	

	def get_data(self, country):
		self.zipCodes.get_data(country)

	def delete(self):
		self.zipCodes.delete()


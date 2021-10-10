#Ernesto Ramírez A01019589 
#Emiliano Peredo A01422326  
#Alejandro López A01173657  
#Valeria Nicole Barra Maldonado A01653899  

from proxy import ProxyZipCodes
import time

z = ProxyZipCodes()
print("Created a connections to the database")
print(z.zipCodes)
print("")
print("Trying to create 2nd connection without deleting the 1st one...")
z2 = ProxyZipCodes()
print("\nGetting data from first connection...")
z.get_data("mexico")

print("\nDeleting first connection")
z.delete()

print("\nNow second connection can initiate")
z3 = ProxyZipCodes()
print(z3.zipCodes)
print("\nGetting data from connection...")
z3.get_data("canada")



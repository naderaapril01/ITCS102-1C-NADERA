
from getpass import getpass

username = 'april'
pword = 'nadera123'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :

         print("Access Granted")
else:
         print("Access Denied")
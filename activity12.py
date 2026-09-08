import getpass
username = 'bambi'
password = 'babadi'

u = input("enter your username --->")
p = getpass.getpass("enter your password --->")

if username == u and password == p :

         print("access granted!")

else:

          print("not today boi")

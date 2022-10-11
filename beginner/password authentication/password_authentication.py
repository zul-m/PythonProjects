import getpass

database = {"john.doe": "123456", "doe.john": "654321"}

username = input("Enter Your Username: ")

password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again: ")
        break
print("Verified")
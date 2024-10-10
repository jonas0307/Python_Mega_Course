username = ''

while username != "pypy":
    username = input("Enter username: ")
    if username == "pypy":
        print ("welcome !")
    else:
        print ("Incorrect username")


while True:
    username = input("Enter username: ")
    if username == "pypy":
        print ("welcome !")
        break
    else:
        print ("Incorrect username")
        continue
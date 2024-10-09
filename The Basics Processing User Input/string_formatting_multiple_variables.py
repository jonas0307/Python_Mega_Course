name = input("Insert your name: ")
surname = input("Insert your surname: ")
#First method 
message = "Hello %s %s " % (name,surname)
#New way introduced on python 3.6
new_message_py36 = f"Hello {name} {surname}"
print (message)
print (new_message_py36)



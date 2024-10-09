user_input = input("Insert your name: ")
#First method 
message = "Hello %s" % user_input
#New way introduced on python 3.6
message_py36 = f"Hello {user_input}"
print (message)
print (message_py36)

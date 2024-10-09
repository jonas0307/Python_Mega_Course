def grettings(name):
    return f"Hi {name.title()}"

message = input ("Insert your name here: ")
output = grettings(message)
print (output)

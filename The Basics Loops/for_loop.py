the_list = [3.5,6.7,8.9]
print ("the list: ",the_list)
for item in the_list:
    print ("The rounded value is: ",round(item))

colors = [11, 34, 98, 43, 45, 54, 54]

for item in colors:
    print (item)

colors = [11, 34, 98, 43, 45, 54, 54]

for item in colors:
    if item > 50:
        print (item)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for item in colors:
    if type(item) == int:
        print (item)


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for item in colors:
    if isinstance(item,int) and item > 50:
        print (item)

the_dictionary = {"Jonas": 43,"Lorena": 33, "Ana Sofia": 9, "Miguel Angel": 2}
print ("The dictionary", the_dictionary)
for item in the_dictionary.items():
    print ("The items", item)

for key in the_dictionary.keys():
    print ("the Key", key)

for value in the_dictionary.values():
    print ("The value", value)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key}: {value}")


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))


    
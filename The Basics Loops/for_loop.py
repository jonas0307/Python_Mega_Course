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



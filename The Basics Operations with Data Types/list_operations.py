the_list = [9.1,4.5,3.0,10.5]
print("The original list",the_list)
#Append
the_list.append(9.3)
print("The list with an item added by append method (9.3)",the_list)
#Clear
the_list.clear()
print("The list after clear method applied",the_list)
the_list = [9.1,4.5,3.0,10.5]
#Index
print("The index of 4.5 value",the_list.index(4.5))
#Index with start
print("The index of 3.0 value starting on 1, is:",the_list.index(3.0,1))
#Remove 
print("The original list",the_list)
the_list.remove(4.5)
print("The list with item removed by remove method (4.5)",the_list)
#Count
print ("The count method of list for 3.0 value",the_list.count(3.0))
the_list.sort()
#Sort
print("The sort method applied",the_list)
the_list = [9.1,4.5,3.0,10.5]
#Sort Reversed
the_list.sort(reverse=True)
print("The sort method applied with reversed=True",the_list)
#Get Value from item
print("The value of item 3 is:",the_list[3])
the_list = [9.1,4.5,3.0,10.5,7.8,3.4,2.6]
#Accesing List Slices
print("The List:",the_list)
print("The lenght of list",len(the_list))
print("The List slice 2-5:",the_list[2:5])
print("Accesing first two items w/o start",the_list[:2])
print("Accesing the last two items w/o finish",the_list[5:])
#Negative indexes
the_list = [9.1,4.5,3.0,10.5,7.8,3.4,2.6]
print("The List:",the_list)
print("Accesing the list items using negative indexes (-2):",the_list[-2])
#Negative also can use the slice of start and finish
#Strings have a list behavior and could be acessed using positive or negative indexing
the_string='Jonas'
print("the string",the_string)
print("the string positive index 1",the_string[1])
print("the string negative index -2",the_string[-2])
the_list_mixed=["Mikkel",1,2.0,3.4]
print("The list_mixed",the_list_mixed)
print("Accesing to the first item string and get the 2nd letter",the_list_mixed[0][1])











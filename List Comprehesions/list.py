print ("################################### ")
temps = [221, 234, 340, 230]
print ("The original list", temps)
#The list comprehension creates a new list using a for 
new_temps = [temp / 10 for temp in temps]
print ("The list divided using list comprehension", new_temps)
print ("############################################")
temps2 = [221, 234, 340, -9999, 230]
print ("New list with a strange number", temps2)
#Using a list comprehension with a conditional if 
new_temps = [ temp / 10 for temp in temps2 if temp != -9999]
print("The new temps without -9999",new_temps)
print ("############################################")
#Only Numbers (E)
#Define a function that takes as a parameter a list that contains both integers and strings
# nd returns the list containing only the integers.
# For example, if I called your function with foo([99, 'no data', 95, 94, 'no data'])
# it should return [99, 95, 94].
def only_integers(the_list):
    new_list = [i for i in the_list if isinstance(i,int)]
    return new_list
    
list_pass = [99, 'no data',95,94,'no data']
print ("The original list",list_pass)
list_result = only_integers(list_pass)
print ("The list clear is:",list_result)
print ("############################################")
#Only Positive Numbers (E)
#Define a function that takes as parameter list of numbers
#and returns the list containing only the numbers that are greater than 0.
# For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].

def only_positive(the_list):
    list_returned = [ value for value in the_list if value >0]
    return list_returned

the_list_parameter = [-5, 3, -1, 101]
print ("The list passed as parameter", the_list_parameter)
list_result2 = only_positive(the_list_parameter)
print ("The list result is: ",list_result2)
print ("############################################")
#Zeros Instead (E)
#Define a function that takes as parameter a list that contains both numbers and strings and returns
#the same list but with zeros instead of strings. 
# For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) 
# it should return [99, 0, 95, 94, 0].

def only_zeros(the_list):
    list_returned = [value if not isinstance(value,str) else 0 for value in the_list]
    return list_returned

the_mixed_list = [99, 'no data', 95, 94, 'no data']
print ("The list passed: ", the_mixed_list)
the_list_proceesed = only_zeros(the_mixed_list)
print ("The list proccesed: ", the_list_proceesed)   
print ("############################################")

#Convert and Sum Up (E)
#Define a function that takes as parameter a list that contains decimal numbers as strings 
#and returns the sum of those numbers.
#For example, I called your function with foo(['1.2', '2.6', '3.3']) 
#it should return 7.1. Note that the floats of the input list are string datatypes.

def sumup(the_list):
    list_returned = sum([float(value) for value in the_list])
    return list_returned

the_list_parameter = ['1.2', '2.6', '3.3']
print ("The list passed: ", the_list_parameter)
the_list_proceesed = sumup(the_list_parameter)
print ("The list proccesed", the_list_proceesed)
print ("############################################")
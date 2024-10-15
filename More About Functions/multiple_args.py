#Function with 2 arguments to calculate the are
print ("################Function with 2 arguments to calculate the area: ################ ")
def area (a,b):
    return a*b

print ("The area is: ",area(5,7))

print("##################Function to concatenates 2 strings ###############################")

def concatenate (str1,str2):
    return str1 + str2
string1="Jonas"
string2="AI"
print ("The string 1:", string1)
print ("The string 1:", string2)
print ("The strings processed by function",concatenate(string1,string2))
print ("###################################################################################")

# Keywords arguments

print ("#########################  Keywords Arguments ######################################")

def division (dividend,divisor):
    return dividend / divisor

print ("Using keywords arguments dividend = 20 and divisor = 4 ", division(dividend=20,divisor=4))
print ("Using keywords arguments dividend = 4 and divisor = 20 ", division(dividend=4,divisor=20))

print ("Using keyword by default where second value == 10")

def multiplication(value1, value2=10):
    return value1 * value2

print ("Result w/o modify second argument: ",multiplication(value1=2))
print ("Result changing second parameter by 8: ", multiplication(value1=2,value2=8))

print("#########################################################################################")

def mean (*args):
        return sum(args) / len(args)


print("The mean using a function with arbitrary number of non-kweywords arguments")

print ("Values to get the mean: 10,23,5,6")
print("The mean of values :", mean(10,23,5,6))
print("#########################################################################################")

print ("Indefinite Number of Strings Processed (E)")

def upper_strings(*args):
    args = [x.upper() for x in args]
    return sorted(args)

input_strings = input("Insert the words: ")

print("The words processed and sorted", upper_strings(input_strings))
print("#########################################################################################")
print("The sum using a function with arbitrary number of keywords arguments")

def find_sum(**kwargs):
    return sum(kwargs.values())
    
    
print(find_sum(x=1, y=2, z=6))
print("#########################################################################################")

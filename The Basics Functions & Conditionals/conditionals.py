def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

the_dic = {"Jonas": 3.5, "Sof": 4.0, "Mikkel": 4.5}
the_list = {2,5,8}

print ("The dictionary", the_dic)
print ("The mean of dictionary using the function",mean(the_dic))

print ("The list", the_list)
print ("The mean of dictionary using the function",mean(the_list))


def temperature(value):
    if value > 7:
        return "Warm"
    else:
        return "Cold"

print(temperature(5))



def pass_controler(value):
    if len(value) >= 8:
        return True
    else:
        return False

print (pass_controler("hola como estas"))


#Elif example

def temperature(value):
    if value > 25:
        return "Hot"
    elif 25 >= value >= 15:
        return "Warm"
    else:
        return "Cold"
        

print (temperature(10))
print (temperature(25))
print (temperature(30))
        
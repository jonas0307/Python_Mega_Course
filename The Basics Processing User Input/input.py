def wheater_condition(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >=20:
        return "Warm"
    else:
        return "Cold"
    
user_input = float(input("Insert the temperature:"))

print(wheater_condition(user_input))
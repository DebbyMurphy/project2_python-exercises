

# fahrenheit = float(26.6)
# celsius = round((fahrenheit - 32) * 5.0/9.0)
# print(celsius)





def celsius_conversion(f):
    f = float(f)
    celsius = (round((fahrenheit - 32) * 5.0/9.0))
    return(celsius)


fahrenheit = [
    32, 
    113, 
    26.6
]

for temps in fahrenheit:
    temps = float(temps)
    print(celsius_conversion(temps))
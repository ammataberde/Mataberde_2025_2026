unit = input("Enter unit (c/f/k): ")
if unit == "f":
    temp = float(input("Enter temperature in Farenheit: "))
    c = (temp - 32) * 5 / 9
elif unit == "k":
    temp = float(input("Enter temperature in Kelvin: "))
    c = temp - 273.15
elif unit == "c":
    temp = float(input("Enter temperature in Celsius: "))
    c = temp
else:
    print("Invalid")
    exit()
if c < 0 :
    print("Too Cold!")
elif c <= 35:
    print("Safe Temperature")
else:
    print("Too Hot!")

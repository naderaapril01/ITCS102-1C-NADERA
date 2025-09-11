temp = int(input("Enter temperature outside (in °C): "))

if temp <= 0:
    print("Temperature is considered freezing.")
elif temp <= 10:
    print("Temperature is considered extremely cold.")
elif temp <= 20:
    print("Temperature is considered cold.")
elif temp <= 30:
    print("Temperature is considered moderately cold.")
elif temp <= 40:
    print("Temperature is considered warm.")
elif temp <= 50:
    print("Temperature is considered hot.")
elif temp <= 100:
    print("Temperature is considered very hot.")
elif temp <= 1000:
    print("Dangerous temperature!")
else:
    print("Invalid or unrealistic temperature.")
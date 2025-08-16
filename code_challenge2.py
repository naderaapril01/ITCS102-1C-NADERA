Gcash = int(input("Enter amount you want to deposit: "))

LOAD1000 = Gcash // 1000
print("This is the breakdown of the amount you deposited:")

print("1000: ", LOAD1000)
Gcash = Gcash - (LOAD1000 * 1000)

LOAD500 = Gcash // 500
print("500: ", LOAD500)
Gcash = Gcash - (LOAD500 * 500)

LOAD200 = Gcash // 200
print("200: ", LOAD500)
Gcash = Gcash- (LOAD200 * 200)

LOAD100 = Gcash // 100
print("100: ", LOAD100)
Gcash = Gcash - (LOAD100 * 100)

LOAD50 = Gcash // 50
print("50: ", LOAD50)
Gcash = Gcash - (LOAD50 * 50)

LOAD20 = Gcash // 20
print("20: ", LOAD20)
Gcash = Gcash - (LOAD20 * 20)

LOAD10 = Gcash // 10
print("10: ", LOAD10)
Gcash = Gcash - (LOAD10 * 10)

print("Remaining coins: ", Gcash)

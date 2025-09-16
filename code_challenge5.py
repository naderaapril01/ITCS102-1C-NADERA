number = eval(input("what is number --> "))
factorial = 0
for a in range(number, 0, -1):
    factorial *= a
print("The factorial of ",number, " is",factorial)
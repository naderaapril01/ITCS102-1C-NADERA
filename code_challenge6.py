j = 5
number = eval(input("how many is number --> "))
factorial = 1 
for j in range(number, 0, -1):
    factorial *= j
print("The factorial of ",number, "is",factorial)   
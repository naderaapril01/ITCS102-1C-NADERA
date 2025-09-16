
import random

total_sum = 0

print("gallery:")

for j in range(10):
    number = random.randint(1, 100)
    print(number)

    if number > 50:
        total_sum += number

print("\n\n\tThe sum of even numbers is:", total_sum)
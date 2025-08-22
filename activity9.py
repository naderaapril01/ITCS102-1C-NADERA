a = 16
b = 15
c = 12
d = 18

print("USER LOGIN")

username = 'april'
password = 'sminedump0101'

print(("username" == 'april') and (password == 'sminedump0101'))

print((a > b) and (c < d))        
print((a > b) or (c < d))           
print(not (a < b) and (c < d))       
print(not (a < b) or (c < d))       

result = ((a < b) and not (c > b) or ((b == a + d and (a != d)) or (c < a)))
print(result)
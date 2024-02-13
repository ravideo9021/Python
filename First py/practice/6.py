#Count the total number of digits in a number

num = int(input("Enter a Number: "))

c = 0
while num > 0:
    c += 1
    num //= 10
    
print(c)
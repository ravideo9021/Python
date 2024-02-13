#Display Numbers from a list

list = [45, 55, 155, 90, 536, 25, 7]

for n in list:
    if n > 500:
        break
    if n % 5 == 0 and n <= 150:
         print(n)
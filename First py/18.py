#pattern printing

#using for loop

for i in range(0, 5):
    for j in range(0, i+1):
        print("* ", end = '')
    print()

for i in range(5, 1, -1):
    for j in range(1, i):
        print("* ", end = '')
    print()

'''
#using while loop

i = 1
while i <= 5:
    j = 0
    while j < i:
        print("* ", end = '')
        j += 1
    print()
    i += 1

i = 5
while i > 1:
    j = 1
    while j < i:
        print("* ", end = '')
        j += 1
    print()
    i -= 1
    
'''
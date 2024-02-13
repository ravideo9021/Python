'''
rh = round_length = 15
rw = round_width = 15

for i in range(8):
    for j in range(8):
        if i :
            print("*", end = '')
        else:
            print(" ", end = '')
    print()
'''
 
for i in range(9):
    for j in range(9-i):
        print(" ", end = '')
    print("*" * (i))
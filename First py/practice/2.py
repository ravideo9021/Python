#pattern printing

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, sep = ' ', end = '')
        j += 1
    print()
    i += 1
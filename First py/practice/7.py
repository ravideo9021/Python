#pattern printing

def pattern():
    p = 1
    q = 5
    while p <= 5:
        while q > 0:
            print(q, end = '')
            q -= 1
        print()
        q = 5 - p
        p += 1
        
        
pattern ()
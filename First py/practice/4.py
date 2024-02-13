#multiplication table

def multiplication_table(n):
    for i in range(10):
        print(f"{n} * {i+1} = { n * (i+1) }")
        
n = int(input("Table of: "))
multiplication_table(n)
 
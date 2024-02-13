def main():
    x = get_int("What is x? ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass  

main()


'''
try:
    x = int(input("what is x? "))
    #print(f"x is {x}")
except ValueError:
    print("x is not an integer")
else :
    print(f"x is {x}")
'''
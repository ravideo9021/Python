#x = float(input("Enter the value of x: "))
#y = float(input("input the value of y: "))

#sum = int(x) + int(y)

#sum = round(x + y)

#z = x / y

#print(f"{z:.2f}")


def main():
    x = int(input("What is x? "))
    print("Square of x is", square(x))
    
def square(n):
    return n * n

main()
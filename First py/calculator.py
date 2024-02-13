def sum(a, b):
    return a +b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    sign = input("choose the operator +, -, *, /: ")
    a = int(input("Enter the first Number: "))
    b = int(input("Enter the second Number: "))

    if sign == '+':
        print("The sum is:", sum(a, b))
    elif sign == '-':
        print("the difference is:", sub(a, b))
    elif sign == '*':
        print("the product is:", multi(a, b))
    elif sign == '/':
        ("the division is:", div(a, b))
    else: print("Not a valid sign")

main()


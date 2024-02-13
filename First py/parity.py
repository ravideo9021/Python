def main():
    x = int (input ("Enter a Number: "))
    if is_even(x):
        print("The given number is 'even'")

    else:
        print("The given number is 'Odd'")


def is_even(x):
    return True if x % 2 == 0 else False

main()
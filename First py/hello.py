def main():
    hello()
    name = input("What is your name: ")
    hello(name)


def hello(to = "World"):
    print("Hello,", to)
    
        
main()
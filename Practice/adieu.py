def takeInput():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            return names


def printNames():
    names = takeInput()
    print("\nAdieu, adieu, to ", end = '')

    if len(names) == 1:
        print(names[0])
        return
    
    if len(names) == 2:
        print(f"{names[0]} and {names[1]}")
        return

    for i in range(len(names)-1):
        print(f"{names[i]}", end = ', ')
        
    print(f"and {names[len(names)-1]}")
    
    return

if __name__ == "__main__":
    printNames()
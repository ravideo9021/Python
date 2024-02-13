def getItem():
    list = []
    
    while True:
        try:
            item = input("Input Item: ")
            list.append(item)
        except EOFError:
            return sorted(list)
        
def makeList():
    groceryList = getItem()
    
    noOfItem = {}

    for item in groceryList:
        noOfItem.append(groceryList.count(item))

        
    print(groceryList)
    print(noOfItem)
        
def main():
    makeList()
    
if __name__ == "__main__":
    main()
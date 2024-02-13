def get_item():
    grocery_list = []
    while True:
        try:
            item = input("").upper()
            grocery_list.append(item)
        except EOFError:
            return sorted(grocery_list)

def arrange_list():
    list = get_item()
    count = {}
    for item in list:
        count[item] = count.get(item, 0) + 1
        
    for item, freq in count.items():
        print(freq, item)
        
def main():
    arrange_list()
    
if __name__ == "__main__":
    main()
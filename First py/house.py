name = input("what is your name: ")

#if name == 'ravi':
#    print("PRABHU")
#    
#elif name == "yash" or name == "rahul" or name == "saurav" or name == "ujjwwal":
#    print("BOYS")
#
#else :
#    print("WHO?")
#
match name:
    case "ravi":
        print("PRABHU")
    case "rahul" | "yash" | "ujjwal" | "saurabh":
        print("BOYS")
    case _:
        print("WHO?")
    
    
fruits = {"apple": 130 ,"avocado" : 50, "banana" : 110 ,"cantaloupe" : 50, "grapefruit" : 60,
          "grapes" : 90 ,"honeydew" : 50, "kiwifruit" : 90, "lemon": 15, "lime" : 20,
          "nectarine" : 60, "orange" : 80, "peach" : 60, "pear" : 100, "pineapple" : 50,
          "Plums" : 70, "Strawberries" : 50, "Sweet Cherries" : 100, "Tangerine" : 50, "Watermelon" : 80}
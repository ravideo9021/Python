def get_menu():
    menu = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
    return menu

def taking_order(menu):
    total_price = 0.00
    while True:
        try:
            user_order = input("Item: ").title()
            total_price += price_calculate(menu, user_order)
            print(f"Total: ${total_price:.2f}")
        except EOFError:
            return
         
              
def price_calculate(menu, user_order):
        if user_order in menu:
            price = float(menu[user_order])
            return price
        else:
            return 0.00
        
        
def main():
    menu = get_menu()
    taking_order(menu)
    
if __name__ == "__main__":
    main()
  
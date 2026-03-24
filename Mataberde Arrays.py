def add_product(products):
    
    name = input("Enter product").strip()
    if not name:
        print("You need to give the product a name.")
        return

    if name in products:
        print("We already have that product")
        return

    try:
        price = float(input(f"How much does '{name}' cost? "))
        if price <= 0:
            print("The price has to be more than zero")
            return  
    except ValueError:
        print("Ivalid price")
        return  

    products[name] = price
    print(f"We added '{name}' to the list.")


def display_products(products):
    if not products:
        print("Add items first")
        return  

    print("Product list:")
    for i, (name, price) in enumerate(products.items()):
        print(f"{i+1}. {name} - ${price:.2f}")  


def update_price(products):
    
    if not products:
        print("Add items first")
        return

    name = input("Which product's price do you want to change? ").strip()
    if name not in products:
        print("Product not found.")
        return  

    try:
        new_price = float(input(f"Enter a new price for '{name}'? "))
        if new_price <= 0:
            print("The price has to be more than zero")
            return  
    except ValueError:
        print("Invalid price")
        return  

    products[name] = new_price
    print(f"Okay, the price for '{name}' is now ${new_price:.2f}.")


def search_product(products):
    if not products:
        print("Add items first")
        return  

    name = input("Enter item").strip()
    if name in products:
        print(f"We got '{name}' and it costs ${products[name]:.2f}.")
    else:
        print("Product not found.")


def main():
    products = {}  

    while True:
        print("\nWhat do you want to do?")
        print("[1] Add a product")
        print("[2] Display all products")
        print("[3] Update a price")
        print("[4] Search for a product")
        print("[5] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(products)
        elif choice == '2':
            display_products(products)
        elif choice == '3':
            update_price(products)
        elif choice == '4':
            search_product(products)
        elif choice == '5':
            print("End")
            break  
        else:
            print("That's not a valid choice. Try again.")


if __name__ == "__main__":
    main()

products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    print("Categories Available:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")
    try:
        category_choice = int(input("Select a category by number: "))
        category_names = list(products.keys())
        if 1 <= category_choice <= len(category_names):
            return category_choice - 1
        else:
            print("Invalid category. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def display_products(products_list):
    print("Products Available:")
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    display_products(sorted_list)
    return sorted_list

def add_to_cart(cart, product, quantity):
    product_name, price = product
    cart.append((product_name, price, quantity))

def display_cart(cart):
    print("\nYour Cart:")
    total_cost = 0
    for item_name, price, quantity in cart:
        item_total = price * quantity
        print(f"{item_name} - ${price} x {quantity} = ${item_total}")
        total_cost += item_total
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\n---- RECEIPT ----")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
    for item_name, price, quantity in cart:
        item_total = price * quantity
        print(f"{quantity} x {item_name} - ${price} = ${item_total}")
    print(f"\nTotal: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    return all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email and len(email.strip()) > 0

def main():
    name = ""
    email = ""

    while not validate_name(name):
        name = input("Enter your name (First Last): ")
        if not validate_name(name):
            print("Invalid name. Please enter your first and last name, separated by a space.")

    while not validate_email(email):
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Invalid email. Please enter a valid email address.")

    cart = []
    while True:
        category_index = None
        while category_index is None:
            category_index = display_categories()

        category_names = list(products.keys())
        selected_category = category_names[category_index]
        product_list = products[selected_category]

        while True:
            display_products(product_list)
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price.")
            print("3. Go back to the category selection.")
            print("4. Finish shopping")

            try:
                option = int(input("Select an option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option == 1:
                try:
                    product_choice = int(input("Enter product number: "))
                    quantity = int(input("Enter quantity: "))
                    if 1 <= product_choice <= len(product_list):
                        selected_product = product_list[product_choice - 1]
                        add_to_cart(cart, selected_product, quantity)
                        print(f"Added {quantity} {selected_product[0]} to your cart.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            elif option == 2:
                sort_order = input("Sort by: 'asc' for Ascending, 'desc' for Descending: ").strip()
                if sort_order in ["asc", "desc"]:
                    product_list = display_sorted_products(product_list, sort_order)
                else:
                    print("Invalid sort order. Please enter 'asc' or 'desc'.")

            elif option == 3:
                break

            elif option == 4:
                if cart:
                    total_cost = sum(price * quantity for _, price, quantity in cart)
                    display_cart(cart)

                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                print("Thank you for shopping with us!")
                return

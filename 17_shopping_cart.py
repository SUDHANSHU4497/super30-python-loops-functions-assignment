"""
Q17. Shopping Cart using Functions
Create functions for add_item(), remove_item(), view_cart(), calculate_total(),
and checkout(). Keep the application running using a while loop until checkout
or exit.
"""

cart = {}


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cart[name] = {"price": price, "quantity": quantity}
    print(name, "added to cart")


def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart:
        del cart[name]
        print(name, "removed from cart")
    else:
        print("Item not found in cart")


def view_cart():
    if len(cart) == 0:
        print("Cart is empty")
    else:
        for name in cart:
            price = cart[name]["price"]
            quantity = cart[name]["quantity"]
            print(name, "- ₹", price, "x", quantity, "=", price * quantity)


def calculate_total():
    total = 0
    for name in cart:
        total = total + cart[name]["price"] * cart[name]["quantity"]
    return total


def checkout():
    view_cart()
    print("Total amount to pay: ₹", calculate_total())
    print("Thank you for shopping!")


while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        print("Total: ₹", calculate_total())
    elif choice == "5":
        checkout()
        break
    elif choice == "6":
        print("Exiting without checkout")
        break
    else:
        print("Invalid choice")

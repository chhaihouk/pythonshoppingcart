import easygui as eg  # Import easygui for GUI dialogs
import json  # Import json to save and load cart history
import os  # Import os to check file existence

# Dictionary with predefined item prices
prices = {
    "apple": 2.00,
    "banana": 1.50,
    "milk": 3.00,
    "bread": 2.50
}

# Dictionary to store the shopping cart (item: quantity)
cart = {}

# File to save cart history
CART_FILE = "cart_history.txt"

# Set the discount threshold and rate
DISCOUNT_THRESHOLD = 20.00  # If total is over $20, apply discount
DISCOUNT_RATE = 0.10        # 10% discount

# Function to show all available items with prices
def show_items():
    items_text = "\n".join([f"{item.capitalize()}: ${price:.2f}" for item, price in prices.items()])  # Format item list
    eg.msgbox(f"Available items:\n\n{items_text}", "Items")  # Show the list to the user

# Function to add an item to the cart
def add_item():
    item = eg.choicebox("Select an item to add:", "Add Item", list(prices.keys()))  # Let user choose item from list
    if item:
        quantity = eg.integerbox("Enter quantity:", "Quantity", lowerbound=1)  # Only allow quantity 1 or more
        if quantity:
            cart[item] = cart.get(item, 0) + quantity  # Add to cart or update quantity
            eg.msgbox(f"Added {quantity} x {item}.", "Item Added")  # Confirm addition

# Function to remove a certain quantity of an item from the cart
def remove_item():
    if not cart:
        eg.msgbox("Your cart is empty.", "Remove Item")  # Show empty cart message
        return
    item = eg.choicebox("Select an item to remove:", "Remove Item", list(cart.keys()))  # Choose item from cart
    if item:
        quantity = eg.integerbox("Enter quantity to remove:", "Remove Quantity", lowerbound=1, upperbound=cart[item])  # Allow partial removal
        if quantity:
            if quantity >= cart[item]:
                del cart[item]  # Remove item completely if quantity equals or exceeds
            else:
                cart[item] -= quantity  # Subtract specified quantity
            eg.msgbox(f"Removed {quantity} x {item}.", "Item Removed")  # Confirm removal

# Function to display the current contents of the cart
def show_cart():
    if not cart:
        eg.msgbox("Your cart is empty.", "Your Cart")  # Show empty cart message
    else:
        cart_text = "\n".join([
            f"{item.capitalize()}: {qty} x ${prices[item]:.2f} = ${prices[item] * qty:.2f}"
            for item, qty in cart.items()
        ])  # Format each item in cart
        eg.msgbox(f"Cart Contents:\n\n{cart_text}", "Your Cart")  # Show the cart

# Function to calculate and display the total bill with discount
def show_total():
    total = sum(prices[item] * qty for item, qty in cart.items())  # Calculate subtotal
    message = f"Subtotal: ${total:.2f}\n"  # Show subtotal
    if total > DISCOUNT_THRESHOLD:
        discount = total * DISCOUNT_RATE  # Calculate discount
        total -= discount  # Apply discount
        message += f"Discount Applied: -${discount:.2f}\n"  # Show discount
    message += f"Total Bill: ${total:.2f}"  # Show final total
    eg.msgbox(message, "Total Bill")  # Display the total

# Function to save the current cart to file
def save_cart():
    with open(CART_FILE, "w") as f:
        json.dump(cart, f)  # Save cart as JSON
    eg.msgbox("Cart saved successfully.", "Save Cart")  # Confirm save

# Function to load cart from file if exists
def load_cart():
    global cart
    if os.path.exists(CART_FILE):
        with open(CART_FILE, "r") as f:
            cart = json.load(f)  # Load cart from file
        eg.msgbox("Previous cart loaded.", "Cart Loaded")  # Confirm load
    else:
        eg.msgbox("No saved cart found.", "Cart Load")  # Inform no file

# Load cart at start
load_cart()

# Main program loop
while True:
    choice = eg.buttonbox(
        "Choose an option:",
        "Shopping Cart",
        ["Add Item", "Remove Item", "View Cart", "Display Total", "Save Cart", "Exit"]
    )  # Show menu options

    if choice == "Add Item":
        add_item()  # Add item
    elif choice == "Remove Item":
        remove_item()  # Remove item
    elif choice == "View Cart":
        show_cart()  # View cart
    elif choice == "Display Total":
        show_total()  # Show total
    elif choice == "Save Cart":
        save_cart()  # Save cart
    elif choice == "Exit":
        save_cart()  # Save on exit
        eg.msgbox("Thank you for shopping! Your cart was saved.", "Goodbye")  # Exit message
        break  # Exit loop

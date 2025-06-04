import easygui as eg

# Dictionary with predefined item prices
prices = {
    "apple": 2.00,
    "banana": 1.50,
    "milk": 3.00,
    "bread": 2.50
}

# Dictionary to store the shopping cart (item: quantity)
cart = {}

# Set the discount threshold and rate
DISCOUNT_THRESHOLD = 20.00  # If total is over $20, apply discount
DISCOUNT_RATE = 0.10        # 10% discount

# Function to show all available items with prices
def show_items():
    # Create a string listing items and their prices
    items_text = "\n".join([f"{item.capitalize()}: ${price:.2f}" for item, price in prices.items()])
    # Show the list to the user in a message box
    eg.msgbox(f"Available items:\n\n{items_text}", "Items")

# Function to add an item to the cart
def add_item():
    show_items()  # Show available items first
    item = eg.enterbox("Enter item to add:", "Add Item")  # Ask for item name
    if item:
        item = item.lower()
        if item in prices:  # Check if item is valid
            try:
                quantity = int(eg.enterbox("Enter quantity:", "Quantity"))  # Ask for quantity
                if quantity > 0:  # Only allow positive quantities
                    cart[item] = cart.get(item, 0) + quantity  # Add to cart or update quantity
                    eg.msgbox(f"Added {quantity} x {item}.", "Item Added")  # Confirm addition
                else:
                    eg.msgbox("Please enter a quantity greater than 0.", "Invalid Quantity")
            except (ValueError, TypeError):
                eg.msgbox("Please enter a valid number for quantity.", "Error")  # Handle invalid input
        else:
            eg.msgbox("Item not available.", "Error")  # Item not in price list

# Function to remove an item from the cart
def remove_item():
    if not cart:
        eg.msgbox("Your cart is empty.", "Remove Item")  # Cart empty message
        return
    show_cart()  # Show current cart contents first
    item = eg.enterbox("Enter item to remove:", "Remove Item")  # Ask for item to remove
    if item:
        item = item.lower()
        if item in cart:  # If item is in cart
            del cart[item]  # Remove it
            eg.msgbox(f"Removed {item}.", "Item Removed")  # Confirm removal
        else:
            eg.msgbox("Item not found in cart.", "Error")  # Item not found message

# Function to display the current contents of the cart
def show_cart():
    if not cart:
        eg.msgbox("Your cart is empty.", "Your Cart")  # Cart empty message
    else:
        # List each item, quantity, and cost
        cart_text = "\n".join([
            f"{item.capitalize()}: {qty} x ${prices[item]:.2f} = ${prices[item] * qty:.2f}"
            for item, qty in cart.items()
        ])
        eg.msgbox(f"Cart Contents:\n\n{cart_text}", "Your Cart")  # Show cart details

# Function to calculate and display the total bill with discount
def show_total():
    total = sum(prices[item] * qty for item, qty in cart.items())  # Calculate subtotal
    message = f"Subtotal: ${total:.2f}\n"
    if total > DISCOUNT_THRESHOLD:  # If total qualifies for discount
        discount = total * DISCOUNT_RATE  # Calculate discount amount
        total -= discount  # Subtract discount from total
        message += f"Discount Applied: -${discount:.2f}\n"
    message += f"Total Bill: ${total:.2f}"  # Show final total
    eg.msgbox(message, "Total Bill")

# Main program loop - shows menu and processes user choices
while True:
    choice = eg.buttonbox(
        "Choose an option:",
        "Shopping Cart",
        ["Add Item", "Remove Item", "View Cart", "Display Total", "Exit"]
    )

    if choice == "Add Item":
        add_item()  # Call add item function
    elif choice == "Remove Item":
        remove_item()  # Call remove item function
    elif choice == "View Cart":
        show_cart()  # Call function to show cart
    elif choice == "Display Total":
        show_total()  # Call function to show total bill
    elif choice == "Exit":
        eg.msgbox("Thank you for shopping!", "Goodbye")  # Exit message
        break  # End program

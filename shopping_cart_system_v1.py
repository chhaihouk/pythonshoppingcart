# Version 1 - Basic Shopping Cart Program

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

# Function to display the main menu
def display_menu():
    print("\n--- Shopping Cart Menu ---")  # Menu title
    print("1. Add Item")                  # Option 1
    print("2. Remove Item")               # Option 2
    print("3. Display Total Bill")        # Option 3
    print("4. Exit")                      # Option 4

# Function to add an item to the cart
def add_item():
    print("Items can add are, apple, banana, milk, bread") # Shows the user the opt
    item = input("Enter item name: ").lower()  # Ask for item name and convert to lowercase
    if item in prices:                         # Check if item exists in price list
        quantity = int(input("Enter quantity: "))  # Ask for quantity and convert to integer
        cart[item] = cart.get(item, 0) + quantity  # Add to cart or update quantity
        print(f"{quantity} x {item} added to cart.")  # Confirmation message
    else:
        print("Item not available.")  # Show message if item doesn't exist

# Function to remove an item from the cart
def remove_item():
    print("Items can remove are, apple, banana, milk, bread")
    item = input("Enter item name to remove: ").lower()  # Ask for item name
    if item in cart:                                     # Check if item is in the cart
        del cart[item]                                   # Remove the item from the cart
        print(f"{item} removed from cart.")              # Confirmation message
    else:
        print("Item not found in cart.")  # Show message if item is not in cart

# Function to display the total bill
def display_total():
    total = 0  # Start with total = 0
    for item, quantity in cart.items():                        # Loop through cart items
        total += prices[item] * quantity                       # Add item price × quantity to total
    print(f"\nSubtotal: ${total:.2f}")                         # Show subtotal before discount

    if total > DISCOUNT_THRESHOLD:                             # If total is over the discount threshold
        discount = total * DISCOUNT_RATE                       # Calculate discount
        total -= discount                                      # Subtract discount from total
        print(f"Discount applied: -${discount:.2f}")           # Show discount amount

    print(f"Total Bill: ${total:.2f}")                         # Show final total

# Main loop to run the program until user exits
while True:
    display_menu()                                # Show the menu
    choice = input("Choose an option (1-4): ")    # Get user choice

    if choice == "1":             # If user chooses 1
        add_item()                # Call function to add item
    elif choice == "2":           # If user chooses 2
        remove_item()             # Call function to remove item
    elif choice == "3":           # If user chooses 3
        display_total()           # Call function to show total bill
    elif choice == "4":           # If user chooses 4
        print("Thank you for shopping. Goodbye!")  # Exit message
        break                     # Exit the loop and end the program
    else:
        print("Invalid choice. Please enter 1-4.")  # Handle invalid input

items = {
    'Tea☕': 24,
    'Pizza Mini🍕': 180,
    'Dosa': 80
}

print('Hello! Welcome to OurCafe 🏤')
print('Here is our menu 🍽:\n')


for item, price in items.items():
    print(f"{item}: ₹{price}")


order = input("\nPlease enter your order exactly as in menu: ")

if order in items:
    quantity_input = input("Enter the quantity: ")
    
   
    if quantity_input.isdigit():
        quantity = int(quantity_input)
        total_price = items[order] * quantity
        print(f"\nYour total bill is: ₹{total_price}")
        print("Thank you! Please visit again 😊")
    else:
        print("Invalid quantity entered. Please enter a valid number.")
else:
    print("Sorry, we don't have that item.")

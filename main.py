from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int

# Function to calculate total value
def total_value(product):
    return product.price * product.quantity

# List to store all products
products = []
# Control variable for loop
# Product Name
while True:
    name = input("Enter product name: ")
# Price Validation
    while True:
        try:
            price = float(input("Enter price: R"))
            break
        except ValueError:
            print("Please enter a valid number.")
# Quantity Validation
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Please enter a whole number.")
  # Create Product Object
  # Add Product Object to List
    product = Product(name, price, quantity)
    products.append(product)
 # Ask user if they want to continue
    choice = input("Capture another product? (yes/no): ").lower()

    if choice != "yes":
        break

# Display Summary
print("\n--- Inventory Summary ---")

total_inventory = 0

for product in products:
    value = total_value(product)
    print(f"{product.name}: R{product.price:.2f} x "
          f"{product.quantity} = R{value:.2f}")
    total_inventory += value

print(f"\nTotal inventory value: R{total_inventory:.2f}")

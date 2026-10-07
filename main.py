from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int


def total_value(product):
    return product.price * product.quantity


products = []

while True:
    name = input("Enter product name: ")

    while True:
        try:
            price = float(input("Enter price: R"))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Please enter a whole number.")

    product = Product(name, price, quantity)
    products.append(product)

    choice = input("Capture another product? (yes/no): ").lower()

    if choice != "yes":
        break


print("\n--- Inventory Summary ---")

total_inventory = 0

for product in products:
    value = total_value(product)
    print(f"{product.name}: R{product.price:.2f} x "
          f"{product.quantity} = R{value:.2f}")
    total_inventory += value

print(f"\nTotal inventory value: R{total_inventory:.2f}")
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    # 1. Internalized logic into an instance method
    def total_value(self) -> float:
        return self.price * self.quantity

# 2. Reusable validation helpers to clean up the main loop
def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Please enter a valid number.")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Please enter a whole number.")

products = []

# Main Input Loop
while True:
    name = input("\nEnter product name: ").strip()
    if not name:
        print(" Product name cannot be empty.")
        continue

    price = get_float_input("Enter price: R")
    quantity = get_int_input("Enter quantity: ")
    
    # Create and add object
    products.append(Product(name, price, quantity))
    
    # Simplified choice check
    if input("Capture another product? (yes/no): ").lower().strip() != "yes":
        break

# Display Summary
print("\n--- Inventory Summary ---")

for p in products:
    print(f" {p.name}: R{p.price:.2f} x {p.quantity} = R{p.total_value():.2f}")

# 3. Clean list comprehension for total calculation
total_inventory = sum(p.total_value() for p in products)
print(f"\n Total inventory value: R{total_inventory:.2f}")

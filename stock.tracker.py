print("Welcome to Stock Portfolio Tracker")

name = input("Enter your name: ")
stock = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per share: "))

total = quantity * price

print("\n--- Portfolio Summary ---")
print("Name:", name)
print("Stock:", stock)
print("Quantity:", quantity)
print("Price per share:", price)
print("Total Investment:", total)
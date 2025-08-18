age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print(f"Ticket price: ${price}") # here f is for formatting strings

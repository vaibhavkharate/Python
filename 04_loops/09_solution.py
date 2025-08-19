items = ["apple", "banana", "cherry"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item found:", item)
        break
    unique_items.add(item)
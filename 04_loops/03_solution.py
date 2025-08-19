number = 3

for i in range(1, 11):
    if i == 5:
        continue # Skip the rest of the loop when i is 5
    print(number, "x", i, "=", number * i)
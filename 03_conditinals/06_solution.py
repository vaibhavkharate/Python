distance = 5

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "Car"

print("AI recommends you to transport with", transport)
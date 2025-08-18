password = "Password@123"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "good"
else:
    strength = "strong"

print ("Your Password Strength is", strength)
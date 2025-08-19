number = 29

is_prime = True

# if number > 1:
for i in range(2, int(number**0.5) + 1): # the logic here is to check for factors up to the square root of the number
    # in detailed like int(number**0.5) + 1 gives the range of possible factors
# for i in range(2, number):        
    if (number % i) == 0:
        is_prime = False
        break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

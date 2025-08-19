while True:
    number = int(input("Enter a number (1 to 10): "))
    if 1 <= number <= 10:
        print("You entered:", number)
        break
    else:
        print("Invalid input. Please try again.")
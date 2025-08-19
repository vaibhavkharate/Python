input_str = "auaubavhababbac"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Unique character found:", char)
        break
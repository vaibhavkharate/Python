Score = 99

if Score >= 101:
    print("Please verify your Score again")
    exit() # To exit the program

if Score >= 90:
    grade = "A"
elif Score >= 80:
    grade = "B"
elif Score >= 70:
    grade = "C"
elif Score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

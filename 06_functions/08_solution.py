def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="Wonderland")
print_kwargs(country="USA", language="English")
print_kwargs()  # No arguments passed
print_kwargs(name="Bob")  # Single argument passed

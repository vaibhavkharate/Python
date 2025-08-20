def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i # yield is remembered the function's state and the value where it left off

for num in even_generator(10):
    print(num)

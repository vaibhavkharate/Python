def sum_all(*args): # there are possibilities of multiple arguments 
    print(f"Arguments received: {args}")
    for i in args:
        print (i * 2)
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))  # Output: 15
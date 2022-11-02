def fibGenerator(fib):
    fib1, fib2 = 0, 1
    for i in range(fib):
        if fib2 > fib:
            break 
        yield fib2
        fib1, fib2 = fib2, fib1+fib2


for i in fibGenerator(1000000):
    print(i)

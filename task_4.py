def fib(n):    # Print Fibonacci series up to n

    a, b = 0, 1

    while a < n:

        print(a, end=' ')

        a, b = b, a+b

    print()


# Now call the function we just defined:

fib(2000)

# More information and more examples available at: https://docs.python.org/3.11/tutorial/controlflow.html
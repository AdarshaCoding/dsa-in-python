def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number: "))
if n <= 0:
    print("Please enter a postive number")
else:
    print(f"Fibonacci Series for {n} : ", end="")
    for i in range(n):
        print(fibonacci(i), end=" ")

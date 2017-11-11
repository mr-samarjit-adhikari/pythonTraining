
def fib(n):
    "Calculate the Fibonacci numbers (in Python)."
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    for i in range(5):
        print(fib(i))

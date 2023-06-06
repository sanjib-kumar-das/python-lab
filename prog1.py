# write a progrma that cumputes nth fibonacci number where n is the value inputted by user

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter a number: "))
print(fib(num))
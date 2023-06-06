# write a program that accepts a value of n as input and determines if the value is prime. if n is not prime the program should quit as soon as it finds a value that evenly divides n

def main():
    n = eval(input("Enter a number: "))
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")

main()
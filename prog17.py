# Write a program that asks the user to enter a number and prints the sum of the divisors of that number.


def main():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + i
    print(sum)
    if __name__ == "__main__":
        main()

main()
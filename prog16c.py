# Write a program that asks the user to enter a power and how many digits they want. Find the last that many digits of 2 raised to the power the user entered.

def main():
    power = int(input("Enter the power: "))
    digits = int(input("Enter the number of digits: "))
    print((2 ** power)%(10 ** digits))
    if __name__ == "__main__":
        main()

main()
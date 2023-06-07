# write a program that uses a while loop to determine how long it takes to double an investment at a given interest rate


def main():
    print("This program calculates how long it takes to double an investment at a given interest rate.")
    print()

    rate = float(input("Enter the annual interest rate: "))
    principal = 1
    years = 0
    while principal < 2:
        principal += principal * (rate/100)
        years += 1
    print("It takes", years, "years to double your investment.")

if __name__ == "__main__":
    main()
# One way to find out the last digit of a number is to mod the number by 10. Write a program that asks the user to enter a power. Then find the last digit of 2 raised to that power.


def main():
    power = eval(input("Enter a power: "))
    print(2 ** power % 10)
    if __name__ == "__main__":
        main()

main()
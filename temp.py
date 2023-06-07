# write a program to find factors of a given number


def main():
    print("This program calculates the factors of a given number")
    number = int(input("Please enter the number: "))
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
if __name__ == "__main__":
    main()
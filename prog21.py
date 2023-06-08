# write a program that asks the user for an interger and creates a list that consists of the factors of that onteger

def main():
    print("This program calculates the factors of a given number")
    number = int(input("Please enter the number: "))
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(factors)
if __name__ == "__main__":
    main()



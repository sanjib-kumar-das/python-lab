# Write a program to find all numbers 1 and 1000 that are divisible by 7 and end in a 6

def main():
    print("This program finds all numbers 1 and 1000 that are divisible by 7 and end in a 6")
    for i in range(1,1001):
        if i % 7 == 0 and i % 10 == 6:
            print(i)
if __name__ == "__main__":
    main()
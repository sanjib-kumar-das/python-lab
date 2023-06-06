# Ask the user for a number and then print the following, where the pattern ends at the Number that the user enters.
# 1
#    2
#       3
#          4


def main():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(" " * (i - 1), i, sep = "")
    if __name__ == "__main__":
        main()

main()
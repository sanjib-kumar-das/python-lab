# Write a function called matches that takes two strings as arguments and returns how many matches there are between the strings. A match is where the two strings have the same character at the same index

def matches(s1,s2):
    count = 0
    for i in range(len(s2)):
        if s1[i] == s2[i]:
            count += 1
    return count
def main():
    s1 = input("Please enter the first string: ")
    s2 = input("Please enter the second string: ")
    print("The number of matches are: ",matches(s1,s2))
if __name__ == "__main__":
    main()
# Write a program that asks the user to enter two strings of the same length. The program should then check to see if the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they are of the same length, the program should alternate the characters of the two strings. For example, if the user enters abcde and ABCDE the program should print out AaBbCcDdEe.

def main():
    string1 = input("Enter a string: ")
    string2 = input("Enter another string of same length: ")
    if len(string1) != len(string2):
        print("The strings are not of the same length.")
        return
    new_string = ""
    for i in range(len(string1)):
        new_string = new_string + string1[i] + string2[i]
    print(new_string)

main()
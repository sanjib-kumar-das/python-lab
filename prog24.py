# Adding certain numbers to their reversals sometimes produces a palindromic number. For instance, 241 + 142 = 383. Sometimes, we have to repeat the process. For instance, 84 + 48 =132 and 132 + 231 = 363. Write a program that finds both two-digit numbers for which this process must be repeated more than 20 times to obtain a palindromic number

def main():
    print("This program finds both two-digit numbers for which this process must be repeated more than 20 times to obtain a palindromic number")
    for i in range(10,100):
        number = i
        for j in range(20):
            number = number + int(str(number)[::-1])
            if str(number) == str(number)[::-1]:
                break
        if j == 19:
            print(i)
    print("Found on iteration no: ",number)
if __name__ == "__main__":
    main()
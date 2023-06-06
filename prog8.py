# Formula for computing easter in the years 1982-2048, as follws: let a = year%19, b = year%4, c = year%7, d = (19a+24)%30, e = (2b+4c+6d+5)%7. The date of easter is march 22 +d+e (which could be in april). Write a program that inputs a year, verifies is it in the range and then prints the date of easter that year

def easter(year):
    if year < 1982 or year > 2048:
        print("Year must be between 1982 and 2048")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        if d + e < 10:
            print("Easter is March", 22+d+e)
        else:
            print("Easter is April", d+e-9)

year = int(input("Enter a year: "))
easter(year)
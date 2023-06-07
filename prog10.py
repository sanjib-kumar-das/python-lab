# calculate day number from date and month


def main():
    print("This program calculates the day number within the year")
    print("for a date that you will enter.")

    date = int(input("Please enter the date: "))
    month = int(input("Please enter the month: "))
    year = int(input("Please enter the year: "))

    if(year % 4 != 0 or year % 400 != 0):
        day = 31 * (month - 1) + date
        if month > 2:
            day = day - ((4 * month) + 23) // 10
    elif (year % 4 == 0 or year % 400 == 0):
        day = 31 * (month - 1) + date
        if month > 2:
            day = day - ((4 * month) + 23) // 10
            day = day + 1
    print("The day number is", day)
    
if __name__ == "__main__":
    main()





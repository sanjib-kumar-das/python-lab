#write a program that accepts a date in the form of month/day/year and outputs whether tha date is valid or not. for eg: 5/24/2020 is valid but 9/31/2004 is not valid as september has only 30 days

def valid_date(date):
    date = date.split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    if month < 1 or month > 12:
        print("Invalid date")
    elif day < 1 or day > 31:
        print("Invalid date")
    elif month == 2 and day > 29:
        print("Invalid date")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print("Invalid date")
        else:
            print("Valid date")
    else:
        print("Valid date")

date = input("Enter a date in the form of month/day/year: ")
valid_date(date)
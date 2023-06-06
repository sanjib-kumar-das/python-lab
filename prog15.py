# write a program that computes the fuel efficiency of a multi-leg journey. the program will first prompt for startingm odometer reading and then get information about a series of legs. for each leg, the user enters the current odometer reading and the amount of gas used (separated by space). the user signals the end of trip with a blank line. the program should print the miles per gallon achieved on each leg and the total MPG for the trip


def main():
    # get the starting odometer reading
    odoStart = int(input('What is the starting odometer reading? '))

    # initialize total miles and total fuel consumed to zero
    milesTtl = 0; fuelTtl = 0

    # get the next odometer reading and fuel consumption, separated by a space
    odoFuel = input('\nEnter the odometer reading and fuel consumption for this leg of the trip, separated by a space: ')

    # loop while entered text is not empty
    while odoFuel != '' and len(odoFuel.split()) == 2:
        # split entered text into odometer reading and fuel consumption
        strList = odoFuel.split()
        odoNext = int(strList[0])
        fuelNext = int(strList[1])

        # print mpg for this leg (current - (start + total miles)) / fuel consumed
        print('Fuel efficiency for this leg: {:.1f}'.format((odoNext - (odoStart + milesTtl)) / fuelNext))

        # update total miles with current odometer reading - starting reading
        milesTtl = odoNext - odoStart

        # update total fuel consumed
        fuelTtl += fuelNext

        # get the next odometer reading and fuel consumption, separated by a space
        odoFuel = input('\nEnter the odometer reading and fuel consumption for this leg of the trip, separated by a space: ')

    # print mpg for entire trip (total miles / total fuel)
    if fuelTtl > 0:
        print('\nFuel efficiency for entire trip: {:.1f}\n'.format(milesTtl / fuelTtl))
    else:
        print('\nInsufficient data was entered.')

if __name__ == '__main__':
    main()
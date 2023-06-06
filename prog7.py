# The speeding ticket fine policy is $50 plus $5 for each mph over the limit plus a penalty of $200 for any speed over 90mph. write a program that accepts aa speedlimit and a clocked speed and either prints a message indicating the speed was legal or the amount of fine if the speed is illegal

def speeding_ticket(speed_limit, clocked_speed):
    if clocked_speed <= speed_limit:
        print("Speed was legal")
    elif clocked_speed <= 90:
        fine = 50 + (clocked_speed - speed_limit) * 5
        print("Fine: $", fine)
    else:
        fine = 50 + (clocked_speed - speed_limit) * 5 + 200
        print("Fine: $", fine)

speed_limit = int(input("Enter the speed limit: "))
clocked_speed = int(input("Enter the clocked speed: "))
speeding_ticket(speed_limit, clocked_speed)
def calculate_mpg(start_odometer, end_odometer, fuel_used):
    distance = end_odometer - start_odometer
    mpg = distance / fuel_used
    return mpg

def compute_fuel_efficiency():
    start_odometer = float(input("Enter the starting odometer reading: "))
    total_distance = 0
    total_fuel_used = 0

    while True:
        input_line = input("Enter the current odometer reading and fuel used (separated by space), or press Enter to end the trip: ")
        
        if input_line == "":
            break

        current_odometer, fuel_used = map(float, input_line.split())

        leg_distance = current_odometer - start_odometer
        leg_fuel_used = fuel_used
        leg_mpg = calculate_mpg(start_odometer, current_odometer, fuel_used)

        print(f"Miles per gallon for leg: {leg_mpg:.2f}")

        total_distance += leg_distance
        total_fuel_used += leg_fuel_used
        start_odometer = current_odometer

    if total_fuel_used == 0:
        print("No fuel consumption information provided.")
    else:
        total_mpg = calculate_mpg(start_odometer, start_odometer + total_distance, total_fuel_used)
        print(f"\nTotal miles per gallon for the trip: {total_mpg:.2f}")

compute_fuel_efficiency()

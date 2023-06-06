# write a program that uses a while loop to determinje how long it takes for an investmnt to double at a given interest rate. the input will be an annualised interest rate, and output is the number of year it takes an investment to double. note the amount of intial investment does not matter, you can use 1$


principal = 1
interest = eval(input("Enter annual interest rate in decimal: "))
year = 0

while balance < 2*principal:
    balance = balance*(1+interest)
    year += 1

print("Years to double: ", year)
# write a program that approximates the value of pi by summing the series 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ... also check accuracy with math.pi

import math

def approx_pi(n):
    pi = 0
    for i in range(n):
        if i % 2 == 0:
            pi += 4/(2*i+1)
        else:
            pi -= 4/(2*i+1)
    return pi
def pi_error(n):
    return math.pi - approx_pi(n)

num = int(input("Enter the number of terms: "))
print(approx_pi(num))
print("Error in calculation: ",pi_error(num))
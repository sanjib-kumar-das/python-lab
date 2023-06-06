# Let us write a program that generates 10000 random numbers between 1 and 100 and counts how many of them are multiples of 12.

import random
def gen_random_num():
    count = 0
    for i in range(10000):
        num = random.randint(1,100)
        print(num)
        if num % 12 == 0:
            count += 1
    print("Number of multiples of 12: ", count)
gen_random_num()

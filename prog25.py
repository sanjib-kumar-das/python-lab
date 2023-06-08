# Write a function that returns the digital root of an integer n

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))
    
def main():
    n = int(input("Please enter the number: "))
    print(digital_root(n))
if __name__ == "__main__":
    main()


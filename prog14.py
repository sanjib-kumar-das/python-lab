# find gcd of two numbers using euclid's algorithm

def gcd(a, b):

	if (a == 0):
		return b
	if (b == 0):
		return a	
	if (a == b):
		return a
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)


a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

print('GCD of', a, 'and', b, 'is', gcd(a, b))



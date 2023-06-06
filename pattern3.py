#Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.

# *
# **
# ***
# ****
# *****

rows = int(input("Please Enter the Total Number of Rows  : "))
print("Rectangular Pattern of Stars:-")
for i in range(rows):
    for j in range(i+1):
        print('*', end = '  ')
    print()

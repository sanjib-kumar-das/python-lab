#Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box should be.

# *******************
# *                 *
# *                 *
# *******************

rows = int(input("Please Enter the Total Number of Rows: "))
cols = int(input("Please Enter the Total Number of Columns:"))
print("Rectangular Pattern of Stars:-")
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()

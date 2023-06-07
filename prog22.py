# write a program that removes any repeated items from a list so that each item appears at most once.

def main():
    print("This program removes any repeated items from a list so that each item appears at most once.")
    list1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
if __name__ == "__main__":
    main()
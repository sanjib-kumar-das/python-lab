# write a program that removes any repeated items from a list so that each item appears at most once

def main():
    user_list = input("Please enter a list of numbers separated by a comma: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    print(user_list)
    new_list = []
    for i in user_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
if __name__ == "__main__":
    main()
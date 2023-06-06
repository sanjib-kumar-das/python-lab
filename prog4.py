# write a program which calculate the numeric value of a given name

def name_value(name):
    name = name.upper()
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value
if __name__ == '__main__':
    name = input("Enter a name: ")
    print(name_value(name))


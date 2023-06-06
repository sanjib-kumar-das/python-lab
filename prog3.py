# Write a program that allows user to write a phrase and output will be the acronym of that


def acronym(phrase):
    phrase = phrase.split()
    acronym = ""
    for word in phrase:
        acronym += word[0]
    return acronym.upper()

phrase = input("Enter a phrase: ")
print(acronym(phrase))
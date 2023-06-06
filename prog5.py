# write a program that counts the number of words in a sentence

def word_count(sentence):
    sentence = sentence.split()
    return len(sentence)

sentence = input("Enter a sentence: ")
print(word_count(sentence))
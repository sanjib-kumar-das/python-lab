# write a program that calculates the average word length in a sentence

def word_length(sentence):
    sentence = sentence.split()
    length = 0
    for word in sentence:
        length += len(word)
    return length / len(sentence)

sentence = input("Enter a sentence: ")
print(word_length(sentence))

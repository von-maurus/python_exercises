import sys

line = sys.stdin.newlines

print(line)

"""print_lines is a function that prints each word on a new line "n" times.
"""


def print_lines(n, word):
    if n != None:
        for i in range(n):
            print(word + "\n")


print_lines(3, "hola mundo")

"""This function takes in a phrase as an argument and prints out the same phrase with each word capitalized except for the first letter. The function first splits the phrase into individual words, then iterates through each word to capitalize all letters except for the first one. The converted phrase is then printed.
"""


def print_phrase_v1(phrase):
    converted_phrase = ""
    words = phrase.split()
    for word in words:
        if word != None:
            newWord = ""
            for index, letter in enumerate(word):
                if index == 0:
                    letter = letter.lower()
                else:
                    letter = letter.upper()
                newWord += letter
            converted_phrase += newWord + " "
    print(converted_phrase)


print_phrase_v1("hola como estas OYE")

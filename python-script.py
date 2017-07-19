#!/usr/local/bin/python
import random

def createMeme():
    phrase = randomUpperLowerCase()

    return print(phrase)

def randomUpperLowerCase():
    txt = input("Enter your phrase: ")
    new_phrase = ''.join(random.choice((x, y)) for x, y in zip(txt.upper(), txt.lower()))
    return new_phrase


if __name__ == '__main__':
    createMeme();
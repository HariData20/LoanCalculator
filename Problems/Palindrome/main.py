from random import random

word = input()
str_length = len(word)
sliced_String = word[str_length::-1]
if word == sliced_String:
    print('Palindrome')
else:
    print('Not palindrome')


word = input()

for c in word:
    if c.isalpha():
        if c in ['a', 'e', 'i', 'o', 'u']:
            print('vowel')
        else:
            print('consonant')
    else:
        break
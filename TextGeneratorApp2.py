#Random generator string
import random, string

vowels='aeiouy'
consonants='bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

#ask user for letters --
#L is letter
Linput_1 = input("What letter do you want? 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
Linput_2 = input("What letter do you want? 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
Linput_3 = input("What letter do you want? 'v' for vowels, 'c' for consonants, 'l' for any letters: ")

def generator():
    if Linput_1 == 'v': letter1  = random.choice(vowels)
    elif Linput_1 == 'c': letter1  = random.choice(consonants)
    elif Linput_1 == 'l': letter1  = random.choice(letters)
    else:
        letter1 = Linput_1

    if Linput_2 == 'v': letter2  = random.choice(vowels)
    elif Linput_2 == 'c': letter2  = random.choice(consonants)
    elif Linput_2 == 'l': letter2  = random.choice(letters)
    else:
        letter2 = Linput_2

    if Linput_3 == 'v': letter3  = random.choice(vowels)
    elif Linput_3 == 'c': letter3  = random.choice(consonants)
    elif Linput_3 == 'l': letter3  = random.choice(letters)
    else:
        letter3 = Linput_3

    Name = letter1 + letter2 + letter3

    return(Name)

for i in range(20):
    print(generator())

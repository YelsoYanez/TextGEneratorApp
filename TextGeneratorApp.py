import random, string

def generator():
    #letter variablles
    letterOne = random.choice(string.ascii_letters)
    letterTwo = random.choice(string.ascii_letters)
    letterThree = random.choice(string.ascii_letters)
    Name = letterOne + letterTwo + letterThree
    return(Name)

print(generator()

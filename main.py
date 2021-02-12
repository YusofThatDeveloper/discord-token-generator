import random
import string
def random_string(length=32):
    character_set = string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))

for i in range(int(input('How many tokens? '))):
    tokens = random_string(24)
    start = ['n','b','z']
    print('Token: ' + random.choice(start) + tokens)
input()
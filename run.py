import random

NUM_OF_GUESSES = 0
MAX_GUESSES = 20
SHIPS = [random.randint(0, 49) for i in range(5)]
CORRECT = 0
PLACE = 0

print('Choose a target between 0 and 49.\n''Hit 3 Battleships to win.\n')
print("       Let's play Battleships       ")
print('     0  1  2  3  4  5  6  7  8  9      ')
for row in range(5):
    location = ' '
    for column in range(10):
        character = ' - '
        location = location + character
    print(row, location)

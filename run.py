import random

num_of_guesses = 0
max_guesses = 20
ships = [random.randint(0, 49) for i in range(5)]
correct = 0
Pplace = 0

print('Choose a target between 0 and 49.\n''Hit 3 Battleships to win.\n')
print("       Let's play Battleships       ")
print('     0  1  2  3  4  5  6  7  8  9      ')
for row in range(5):
    location = ' '
    for column in range(10):
        character = ' - '
        location = location + character
    print(row, location)

used_guesses = []
while num_of_guesses < max_guesses:
    guess = int(input('Choose your target: '))
    num_of_guesses += 1
    if guess in used_guesses and guess in ships:
        correct -= 1
    if guess in used_guesses:
        print('           ALREADY GUESSED!          ')
        num_of_guesses -= 1
        used_guesses.remove(guess)
    used_guesses.append(guess)

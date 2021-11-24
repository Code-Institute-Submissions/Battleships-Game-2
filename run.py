import random

num_of_guesses = 0
max_guesses = 20
ships = [random.randint(0, 49) for i in range(5)]
correct = 0
place = 0

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
    guess = int(input('Choose your target:\n'))
    num_of_guesses += 1
    if guess in used_guesses and guess in ships:
        correct -= 1
    if guess in used_guesses:
        print('           ALREADY GUESSED!          ')
        num_of_guesses -= 1
        used_guesses.remove(guess)
    used_guesses.append(guess)

    place = 0
    print('             Battleships           ')
    print('    0  1  2  3  4  5  6  7  8  9      ')
    for row in range(5):
        location = ' '
        for character in range(10):
            character = ' - '
            if guess == place and guess in ships:
                character = ' X '
                correct += 1
            if guess == place and guess not in ships:
                character = ' O '
            if place in used_guesses and place in ships:
                character = ' X '
            if place in used_guesses and place not in ships:
                character = ' O '
            place += 1
            location = location + character
        print(row, location)

    if guess in ships:
        print('              hit!        ')
    else:
        print('              Miss!        ')

    print('No. of guesses used: ', num_of_guesses)
    print('hits: ', correct)
    print('Total Number of guesses', max_guesses)







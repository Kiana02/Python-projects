import time

user = input("Hey! what's your name? ")
print("Hello, " + user, "let's play hangman!")

#wait for 1 sec
time.sleep(1)

print("Make a guess: ")

time.sleep(0.5)

word = ("elephant")

attempts = ''

turns = 10

while turns > 0:
    fail = 0
    for char in word:

        if char in attempts:

            print(char, end=""),

        else:

            print("_", end=""),
            fail += 1

    if fail == 0:
        print("You won! :)")
        break
    guess = input("Guess a character:")
    attempts += guess
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", + turns, 'more guesses')

        if turns == 0:

            print("You Lose :(")
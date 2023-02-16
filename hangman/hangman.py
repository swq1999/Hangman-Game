import random

# Reading the words.txt file
with open("words.txt", "r") as list:
    words = list.readlines()

# Variables
word = random.choice(words).upper().strip()
lives = len(word)+2
chars = []
done = False

# loop
while not done:
    # Iterating over the wor
    print("") # space
    for c in word:
        if c.upper() in chars:
            print(c, end = " ")
        else:
            print("_", end = " ")
    print("\n") # space

    # User input
    guess = input(f"Lives remaining: {lives}, Your guess: ").strip().upper()
    
    if guess in chars:
        print("You have already guessed that letter.")
    elif guess in word:
        chars.append(guess)
    else:
        lives -= 1
        if lives == 0:
            break
        
    done = True
    for c in word:
        if c.upper() not in chars:
            done = False

# Endgame
if done:
    print(f"\nYou've won!😆 The word was {word}.\n")
else:
    print(f"\nGame over!😓 The word was {word}.\n")
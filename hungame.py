# Hangman Game - Created by Tasneem for Tech Exhibition (2nd Semester)
# Simple Python 3 Program

import random

# Step 1: Hangman stages (displayed one by one when wrong)
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
      _|_
    """,
    """
       ------
       |    |
       |    O
       |
       |
      _|_
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
      _|_
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
      _|_
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
      _|_
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
      _|_
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
      _|_
    """
]

# Step 2: Word list
words = ["apple", "banana", "orange", "grapes", "mango", "cherry", "papaya", "peach"]

# Step 3: Pick a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = len(hangman_stages) - 1
guessed_letters = []

print("🎉 Welcome to the Hangman Game! 🎉")
print("Guess the hidden word letter by letter.\n")

# Step 4: Game loop
while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print(hangman_stages[len(hangman_stages) - 1 - attempts])
    guess = input("Enter a letter: ").lower()

    # Step 5: Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Step 6: Check guess
    if guess in word:
        print("Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!\n")
        attempts -= 1

# Step 7: Game result
if "_" not in guessed_word:
    print("🎊 Congratulations! You guessed the word:", word)
else:
    print(hangman_stages[-1])
    print("💀 Out of attempts! The word was:", word)

print("\nThanks for playing the Hangman Game!")


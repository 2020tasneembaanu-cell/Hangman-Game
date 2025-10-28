# Hangman-Game

A simple and fun **Hangman Word Guessing Game** built using Python — created by **Tasneem** for her **2nd Semester Tech Exhibition**.  
The game randomly selects a fruit name, and the player has to guess it letter by letter before the hangman figure is completed!

---

## 🧠 Features
- Randomly selects a word from a list of fruit names 🍎  
- Tracks correct and incorrect guesses  
- Displays the hangman figure step-by-step  
- Simple, beginner-friendly, and runs entirely in the terminal  

---

## 🧩 How to Play
1. Run the program in Python (`python hangman.py` or `python3 hangman.py`)  
2. The program shows blanks (`_ _ _ _`) for each letter of the word  
3. Enter one letter per turn  
4. Each wrong guess adds one part of the hangman  
5. Guess all letters before the figure completes to win 🎉  

---

## 🧺 Example Output

🎉 Welcome to the Hangman Game! 🎉
Guess the hidden word letter by letter.

Word: _ _ _ _ _
Attempts left: 6

Enter a letter: a
Good guess!

Word: a _ _ _ _
Attempts left: 6

Enter a letter: e
Wrong guess!

   ------
   |    |
   |    O
   |
   |
  _|_


Enter a letter: p
Good guess!
...
🎊 Congratulations! You guessed the word: apple


---

## 🧾 Requirements
- Python 3.x  
- Works on any system (Windows, macOS, Linux)  
- No external libraries needed  

---

## 💡 Author
**Tasneem Banu**  
📍 2nd Semester Tech Exhibition Project  
🎓 Topic: Python Programming – Game Development Basics

---


CODE:
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
words = [
    "apple", "banana", "mango", "orange", "grape", "cherry", "papaya", "peach", 
    "pear", "plum", "kiwi", "lemon", "lime", "melon", "watermelon", "strawberry", 
    "blueberry", "raspberry", "blackberry", "pineapple", "pomegranate", "apricot", 
    "fig", "date", "guava", "lychee", "custardapple", "dragonfruit", "jackfruit", 
    "tamarind", "mulberry", "cranberry", "gooseberry", "persimmon", "starfruit", 
    "avocado", "coconut", "passionfruit", "sapota", "durian", "melon", "cantaloupe", 
    "honeydew", "olive", "breadfruit", "longan", "rambutan", "tangerine", "clementine"
]

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

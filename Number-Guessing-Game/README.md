Number Guessing Game 🎯
Overview

Number Guessing Game is a simple Command Line Interface (CLI) game built with Python. The computer randomly selects a number between 1 and 100, and the player must guess the correct number within a limited number of attempts based on the chosen difficulty level.

The game also includes hints, a timer, and the ability to play multiple rounds.

Features
Random number generation between 1 and 100
Three difficulty levels:
Easy (10 attempts)
Medium (5 attempts)
Hard (3 attempts)
Input validation
Hints after multiple incorrect guesses
Timer to track game duration
Play multiple rounds without restarting the program
Win/Lose conditions
Project Structure
number-guessing-game/
│
├── game.py
└── README.md
Requirements
Python 3.x

No external libraries are required. The project uses only Python standard libraries:

random
time
sys
How to Run

Navigate to the project directory and run:

python game.py

or

python3 game.py

Gameplay
Step 1: Choose Difficulty
1. Easy (10 attempts)
2. Medium (5 attempts)
3. Hard (3 attempts)
Step 2: Guess the Number

Enter a number between 1 and 100.

Example:

Enter your guess:
50
Step 3: Receive Feedback
Too high! Try again.

or

Too low! Try again.
Hint System

After several incorrect guesses, hints are provided:

Hint 1
Hint: The number is even.

or

Hint: The number is odd.
Hint 2
Hint: The number is greater than 50.

or

Hint: The number is 50 or less.
Winning Example
Congratulations! You've guessed the number 42 in 4 attempts!
Game completed in 18.24 seconds.
Losing Example
Game over! You've used all 5 attempts.
The number was 42.
Better luck next time!
Play Again

After each game:

Do you want to play again? (y/n):

Enter:

y

to start a new round.

Enter:

n

to exit the game.

Error Handling

The application handles:

Invalid difficulty selections
Non-numeric input
Incorrect guesses
Invalid game choices

Example:

Please enter a valid number.
Technologies Used
Python
Random Module
Time Module
CLI (Command Line Interface)
Learning Outcomes

This project helped practice:

Python fundamentals
Loops and conditional statements
User input handling
Error handling with try/except
Random number generation
Working with time and timers
Building interactive CLI applications
Program flow control
Future Improvements

Possible enhancements:

High score tracking using JSON
Difficulty-based leaderboards
More advanced hint system
Statistics tracking
Colored terminal output
Save game history
Author

Built as a Python CLI project to practice programming fundamentals and problem-solving skills. 🚀
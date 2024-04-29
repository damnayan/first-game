# first-game
This Python script simulates a simple dice game designed for 2 to 4 players. Each player takes turns rolling a six-sided die to accumulate points. The objective is to reach or exceed a score of 50 points without rolling a 1. Rolling a 1 resets the player's score for that turn to zero and ends their turn immediately.
Key Features:

Player Participation: Supports 2 to 4 players in a single game session.
Interactive Gameplay: Players decide whether to continue their turn by rolling the die or pass to the next player.
Score Tracking: Tracks and updates each player's total score throughout the game.
Instant Feedback: Provides immediate feedback on each die roll and the current score for the turn.
End Game Condition: The game concludes once a player reaches or exceeds 50 points, declaring them the winner.
Technologies Used:

Python 3.
Standard Library: random for die roll simulation
How to Play:

Start the script to initiate the game.
Enter the number of players (between 2 and 4).
Players take turns rolling the die by responding 'y' to continue their turn.
If a player rolls a 1, their turn ends, and any points accumulated during that turn are lost.
The first player to reach or exceed 50 points wins the game.

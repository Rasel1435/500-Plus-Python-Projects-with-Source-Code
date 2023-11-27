"""Rock Paper Scissors Game using Python
To create and play rock paper scissors, I will be using the if and elif statements in Python. I will prepare this game to be played between two
players. Player-1 will be the user, and player-2 will be the computer. Player one will manually select the rock paper or scissor,
while player two will choose randomly. So I will also use the random module in Python to create this game.

I hope you now have understood everything about the rock, paper, and scissors game and how I will create it.
Now, below is how we can write a Python script to create and play rock paper scissors using Python: 
"""

import random

player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player 2 selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
    
    
# output: Select Rock, Paper, or Scissor :Paper
# Player 2 selected:  scissor
# Player 2 Won

""" So this is how you can easily create and play rock, paper, and scissors using the Python programming language as a beginner.
If you are a beginner in Python, you should keep working on such programming projects to improve your programming skills.
You can find some amazing Python practice projects for beginners here. 
"""

"""Summary
So this is how to create and play rock paper scissors using the Python programming language. 
Rock Paper Scissors is a hand game usually played between two people.
In this game, scissors can beat paper, paper can beat rock, and rock can beat scissors.
I hope you liked this tutorial on creating a rock paper scissors using Python.
Feel free to ask valuable questions in the comments section below. 
"""
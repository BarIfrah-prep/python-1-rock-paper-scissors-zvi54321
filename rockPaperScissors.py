# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you want to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""
"""
I am a comment


"""
# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like random and time packages we've discussed about)
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
gameison = True

while gameison:
 userchouce =input("choose your choice rock(1),paper(2),scissors(3)")

 while userchouce != "1" and  userchouce != "2" and userchouce != "3":
    print("invaild choice")
    userchouce = input("choose your choice rock(1),paper(2),scissors(3)")
 else:
     computerchoice=random.randint(1,3)
     userchouce = int(userchouce)

 #case user choose rock

 if userchouce ==1 and computerchoice == 3:
      print("yay you won")
 elif userchouce == 1 and computerchoice ==2:
      print("damm you loss ")
 elif userchouce == 1 and computerchoice == 1:
      print("its a draw!")






#case user choose paper
 if userchouce == 2 and computerchoice == 1:
      print("yay you won")
 elif userchouce == 2 and computerchoice ==3:
      print("damm you loss ")
 elif userchouce == 2 and computerchoice == 2:
      print("its a draw!")






#case user choose scissors
 if userchouce ==3 and computerchoice == 2:
      print("yay you won")
 elif userchouce == 3 and computerchoice ==1:
      print("damm you loss ")
 elif userchouce == 3 and computerchoice == 3:
      print("its a draw!")



 answerreguest = input("wanna continue ? y/n").lower()
 continuereguest = True
 while answerreguest != "y" and answerreguest !="n" and continuereguest:
    print("invalid answer")
    answerreguest = input("wanna continue ? y/n")

 if answerreguest == "y":
     continue
 elif answerreguest == "n":
     print("thanks for playing the game !")
     gameison = False



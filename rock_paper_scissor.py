import random
import os
import time

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=[rock,paper,scissor]
choice_str=["ROCK","PAPER","SCISSORS"]
play="Y"
yes=["y","yes","ya","ja","Ja","Ya","Yes","Y","YES","YA","JA","s","S"]
while(play in yes):
    user=input("------ROCK(1) PAPER(2) SCISSORS(3)------\n Type: \n1 for Rock\n2 for Paper\n3 for Scissors\n-----------------------------------\n")

    try:
        user = int(user)
    except ValueError:
        print("That's not an allowed option.....TRY AGAIN")
    if not (user in [1,2,3]):
        print("Unidentified Option..... TRY AGAIN!!!")
        continue
    computer=random.randint(1,3)
    user=int(user)
    print(("PLAYER CHOICE: "+choice_str[user-1]+"\n"+choices[user-1]).replace('\n', os.linesep))
    print(("COMPUTER CHOICE: "+choice_str[computer-1]+"\n"+choices[computer-1]).replace('\n', os.linesep))
    print(computer,user)
    if(computer==((user+1)%3)):
        print("------------COMPUTER------------------\nWINNER IS COMPUTER\n------------COMPUTER------------------")
    elif(computer==user):
        print("------------DRAW------------------\nNO WINNER---DRAW\n------------DRAW------------------")
    else:
        print("------------PLAYER------------------\nWINNER IS PLAYER\n------------PLAYER------------------")
    play_inp=input("Type YES(Y) to PLAY AGAIN \n  ")
    play=play_inp

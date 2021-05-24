

# Role playing game
# Original J.Timmins 2018
# Updated W.Carr 2021
#------------------------------------------------------------------------------

# Import modules
import random
from random import randint
from time import sleep

#------------------------------------------------------------------------------
# sets the variables for the game | pause is set to 0.5 seconds for speed of the text | turn is set to 0 as the game is starting up for the 1st time | your score is 0 as it starts up
# pause is in caps because it never changes - it is a constant
#------------------------------------------------------------------------------

PAUSE = 0.5
turn = 0
your_score = 0
p2score = 0
lives = 3
spawn = 0

#------------------------------------------------------------------------------

opponents  = ["Mr Smith","Mr Cammack","Mr Birchall","Mr Soulsby","Lord Timmins of Mobberley"]
years = ["1928","2712","1829","2021","1909","1891"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
emotions = ["sad","happy","proud","upset","distraught"]

#subs
def bosses():
    print("----------SETUP----------")
    choices = input("Would you like to add a boss? [y/n]")
    if choices == "y":
        boss = input("What is the name of your boss?")
        opponents.append(boss)
        print("Boss was successfully added.")
    elif choices == "n":
        print("Alright then.")
    else:
        print("Invalid option detected.  Skipping...")

def lives():
    global lives
    live = int(input("How many lives would you like?"))
    lives = live

def selectbos():
    global turn
    global opponent
    global your_score
    global spawn
    
    turn = turn + 1
    opponentcount2 = len(opponents)
    #this picks who your opponent is based on your score
    if your_score < 3:
        spawn = randint(0,2)
    elif your_score < 5:
        spawn = randint(0,3)
    else:
        spawn = randint(0,opponentcount2)

    opponent = opponents[spawn]

def story():
    print("\n")
    print("o===[]:::::::::::::>\n")
    print(f"Turn: {turn}")
    print(f"Lives Remaining: {lives}")
    print(f"Player 1 Score: {your_score}")
    print(f"Player 2 Score: {p2score}")
    sleep(PAUSE)
    day = random.randint(1,28)
    month = random.choice(months)
    year = random.choice(years)
    emotion = random.choice(emotions)
    print(f"It was the {day} {month} {year} and {username} was walking around the halls of AGSB, feeling {emotion}.")
    sleep(PAUSE)
    print("Dark creatures stalk the corridors")
    print()
    sleep(PAUSE)
    print("Out of the shadows steps...")
    sleep(PAUSE)
    print(f"{opponent}!")
    sleep(PAUSE)
    
    print("")
    print(" _\|/^")
    print(" (_oo>")
    print("   |         O")
    print("  /|\\       /|\\")
    print("   |         |")       
    print("   LL        LL")
    print("\n")
    print(opponent + " towers over you. Do you fight, or do you run?")
    print("Enter f or r")
#------------------------------------------------------------------------------

# Main game



#add bosses and lives
bosses()
lives()
username = input("What is your username?")
#while true is a loop so in this case will loop the whole game
while True:
    
    selectbos()

    story()   


    #this checks what the user inputted from f and r for fight and run
    choice = input("> ")

    
    #if the user selected r(run), just print you ran
    #if they type anything else, it will make you a random number between 0 and 5 and add 1 onto it as your "attack"
    #it gets the teachers attack from a random number between 0 and 2 and adding on their spawn value
    #if your attack value is higher than the teachers it prints you fight you win | your opponent is defeated
    #else it prints you fight you lose
    if choice == "r":
        print("You run away, a wise choice")
    else:
        print("Be prepared to meet your doom...")
        sleep(PAUSE)
        # Fill in - what does this instruction do?
        your_attack = (randint(0,5)+1)
        # Fill in - what does this instruction do?
        opponent_attack = randint(0,2) + spawn
        # Fill in - what does this block do?
        if your_attack > opponent_attack:
            print("You fight...you win!")
            print(opponent + " is defeated!")
            your_score = your_score + (spawn+1)
        else:
            print("You fight...you lose!")
        
            lives = lives - 1

            if lives == 0:
                print("GAME OVER")
                exit()
            else:
                h = "h"

 






    

# CLI party game! 
# View the rules on the github page, https://github.com/aleburbridge/Big-Orange-Heads/blob/main/bigorangeheads.py

import os
import random
import time

        # 'name': humanplayer, 
        # 'gold': 0, 
        # 'big_orange_head': 'no', 
        # 'magic wand': 'no', 
        # 'wishes': 3,
        # 'player_number': playerNumber
class player():
    def __init__(self, name, player_number):
        self.name = name
        self.gold = 0
        self.big_orange_head = False
        self.magic_wand = False
        self.wishes = 3
        self.player_number = player_number


def gain_250g(turn):
    for humanplayer in class_list_players:
        if humanplayer.player_number == turn:
            humanplayer.gold += 250

wishGranted = ""

wishListTuples = [
    # gold wishes
    ("Gain 250g", gain_250g),
    ("Gain +100g for 3 turns (300g)", gain_250g),
    ("Gain +75g for 5 turns (375g)", gain_250g),
    ("Gold over time effects are worth +50%", gain_250g),
    ("Gain 250g for each human with a big orange head", gain_250g),
    ("Pick a human to receive 2x gold next gold wish (you can pick yourself)", gain_250g),

    # wishes about wishes
    ("Gain two extra wishes", gain_250g),
    ("Gain an extra wish option next turn", gain_250g),
    ("Guarantee a gold wish option for the next three turns", gain_250g),

    # dice rolls
    ("Roll a d12, gain 10x the gold shown", gain_250g),
    ("Roll a d12. If over 5, +400g. If 5 or under, +100g over 4 turns", gain_250g),

    # wishes that improve odds
    ("Human dice rolls have a 75\% chance to show a 12 (instead of 8%)", gain_250g),
    ("Increase chance for legendary wishes to spawn (10% -> 20%)", gain_250g),

    # items
    ("Genie's lamp (Genie goes back in lamp and humans pick twist)", gain_250g),
    ("Magic piggie bank (100g per turn for the rest of the game)", gain_250g),
    ("Magic Wand (pick a big orange head to remove for 3 turns)", gain_250g),

    #LEGENDAERY
    ("Gain 500g", gain_250g),
    ("Magic Wand (remove 1 orange head)", gain_250g),
    ("Gain extra wish option for rest of game", gain_250g),
    ("30\% chance for twists to fail", gain_250g)
]

clear_screen_command = "cls" if input("Are you on Windows or Mac?\n" +
                                      "Enter W for Windows or anything else for Mac\n> ").strip().lower() == "w" else "clear"
os.system(clear_screen_command)

wishList = []
for tup in wishListTuples:
    wishList.append(tup[0])

twistList = [
    # gold twists
    "Gold over time wishes cost 200g",
    "Next gold wish is deferred two turns",
    "Lose 50g every turn for 5 turns",
    "No gold wishes for two turns",
    "Take all gold from human with least gold",

    # twists about wishes
    "Rock paper scissors the genie for wish to take effect",
    "The wishes for next turn are hidden",
    "The potential twists are hidden next turn",
    "Humans cannot speak to each other next turn",
    "Humans must speak in pig latin next turn",
    "Next turn's wishes are in broken Spanish",
    "Next turn, all twists apply",

    # dice rolls
    "Roll a d12. Humans lose 10x gold of the number shown",
    "Roll a d12. If over 5, the wish fails",
    "Roll a d12. If a 6 or a 9, give a big orange head",

    # big orange heads!
    "Instant gold wishes result in a big orange head",
    "Pick a human to get a big orange head for 3 turns",
    "Humans with a big orange head lose 50g every turn for 3 turns",

    # items
    "Gain 1 magic ticket",
    "Take away item from humans"
]

line_break = "--------------------------------------------------------------------"

def displayIntro():
    
    print('~~~BIG ORANGE HEADS~~~')
    input('press enter to begin :)')


def get_list_players():
    return [x.lower() for x in input("Enter the names of the players separated by a space \n").split()]

def roll_dice():
    print(random.randint(0,12))

def create_suspense():
    for x in range(1, 5):
        b = "Supsense" + "." * x
        print(b, end="\r")
        time.sleep(1)


list_players = get_list_players()
genie_player = list_players[(random.randint(0, (len(list_players) - 1 )))]
list_players.remove(genie_player)
number_of_humans = len(list_players)
totalTurns = number_of_humans * 3
wishesLeft = number_of_humans * 3
playerNumber = 1
class_list_players = []
for idx, player_name in enumerate(list_players):
    class_list_players.append(player(player_name, idx))



# displays info at the top of the screen!
def gold_tracker():
    gold = 0
    for player in class_list_players:
        gold += player.gold
    return gold

humanItems = ['none']
genieItems = ['none']
humanGoldTotal = gold_tracker()
winningGoldAmount = number_of_humans * 500

def dice_roll():
    create_suspense()
    random.randint(0,13)
    
def game_info(turn):
    print("Turn #" + str(turn))
    print("Gold: " + str(humanGoldTotal))
    print("Items: " + str(humanItems))
    print("Wishes left: " + str(wishesLeft))
    player_number_check(turn)

def player_number_check(turn):
    if turn > number_of_humans and turn < (number_of_humans * 2):
        turn -= number_of_humans
    if turn > (number_of_humans * 2):
        turn -= (number_of_humans * 2)
    for humanplayer in class_list_players:
        if humanplayer.player_number == turn:
            humanName = humanplayer.name
            print("Wisher: " + humanName.capitalize() + " (" + str(humanplayer.wishes) + " wishes left)")
            humanplayer.wishes -= 1
            return humanName


def check_answer(grantedwish, turn):
    for wish in wishListTuples:
        if wish[0] == grantedwish:
            wish[1](turn)

firstWish = ("1: " + wishListTuples[random.randint(0, (len(wishList) - 1 ))][0])
secondWish = ("2: " + wishListTuples[random.randint(0, (len(wishList) - 1 ))][0])

def display_wishes(turn):
    global totalTurns
    clear_screen_command
    game_info(turn)
    create_suspense()

    print("~~ WISHES ~~")
    print(firstWish)
    print(line_break)
    print("a. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("b. " + twistList[random.randint(0, (len(twistList) - 1 ))])

    print()
    print(secondWish)
    print(line_break)
    print("a. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("b. " + twistList[random.randint(0, (len(twistList) - 1 ))])

    wisherResponse = input("\n\n")
    if wisherResponse == "1":
        wishGranted = firstWish[3:]
        print(wishGranted)
        check_answer(wishGranted, turn)
    elif wisherResponse == "2":
        wishGranted = secondWish[3:]
        print(wishGranted)
        check_answer(wishGranted, turn)
    turn += 1
    totalTurns -= 1
    ticketChance = input("\n")
    if ticketChance == "ticket":
        print("c. " + twistList[random.randint(0, (len(twistList) - 1 ))])
        input("\n")


def startFirstRound():
    input("Press enter to start the first round!")
    os.system(clear_screen_command)

def startgame():
    displayIntro()
    print()
    create_suspense()
    print("The genie for this game is " + genie_player.capitalize() + "!!!")
    startFirstRound()
wishCounter = len(list_players)

def game_over(winner):
    clear_screen_command
    print(str(winner) + " won!")

startgame()
while True:
    for index in range(1, (number_of_humans * 3)):
        if wishesLeft > 0:
            display_wishes(index)
            gold_tracker()
            wishesLeft -= 1
    if humanGoldTotal == winningGoldAmount:
        game_over(list_players)
    elif totalTurns == 0:
        game_over(genie_player)

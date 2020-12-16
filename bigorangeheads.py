# Text-based party game! 
# View the rules on the github page: ######

import os
import random
import time

clear_screen_command = "cls" if input("Are you on Windows or Mac?\n" +
                                      "Enter W for Windows or anything else for Mac\n> ").strip().lower() == "w" else "clear"
os.system(clear_screen_command)

wishList = [
    # gold wishes
    "Gain 250g",
    "Gain +100g for 3 turns (300g)",
    "Gain +75g for 5 turns (375g)",
    "Gold over time effects are worth +50%",
    "Gain 250g for each human with a big orange head",
    "Pick a human to receive 2x gold next gold wish (you can pick yourself)",

    # wishes about wishes
    "Gain two extra wishes",
    "Gain an extra wish option next turn",
    "Guarantee a gold wish option for the next three turns",

    # dice rolls
    "Roll a d12, gain 10x the gold shown",
    "Roll a d12. If over 5, +400g. If 5 or under, +100g over 4 turns",

    # wishes that improve odds
    "Human dice rolls have a 50\% chance to show a 12 (instead of 8%)",
    "Increase chance for legendary wishes to spawn (10% -> 20%)", # replace these with variables

    # items
    "Genie's lamp (Genie goes back in lamp and humans pick twist)",
    "Magic piggie bank (50g per turn for the rest of the game)",
    "Magic Wand (pick a big orange head to remove for 3 turns)"
]

twistList = [
    # gold twists
    "Gold over time effects cost 200g to use",
    "Next gold wish is deferred two turns",
    "Lose 50g every turn for 5 turns",
    "No gold wishes for two turns",

    # twists about wishes
    "Rock paper scissors the genie for wish to take effect",
    "The wishes for next turn are hidden",
    "The potential twists are hidden next turn",
    "Humans cannot speak to each other next turn",
    "Humans must speak in pig latin next turn",
    "Next turn's wishes are in broken Spanish",

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
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(2)


displayIntro()
print()

list_players = get_list_players()
number_of_players = len(list_players)
genie_player = list_players[(random.randint(0, (int(number_of_players) - 1)))]
dictionary_list_players = []

for item in list_players:
    item = { 
        'name': item, 
        'gold': 0, 
        'big_orange_head': 'no', 
        'magic wand': 'no', 
        'wishes': 3 
        }
    dictionary_list_players.append(item)

# displays info at the top of the screen!
def gold_tracker():
    gold = 0
    for index in range(len(dictionary_list_players)):
        for key in dictionary_list_players[index]:
            if key == 'gold':
                gold += int(dictionary_list_players[index][key])
    return gold



humanItems = []
genieItems = []
humanGoldTotal = gold_tracker()
wishesLeft = ""
winningGoldAmount = number_of_players * 500


def game_info():
    print("gold - " + str(humanGoldTotal))
    print("items - ")

def display_wishes():
    game_info()
    create_suspense()

    print("The wishes for this round are")
    firstWish = ("1: " + wishList[random.randint(0, (len(wishList) - 1 ))])
    secondWish = ("2: " + wishList[random.randint(0, (len(wishList) - 1 ))])
    print(firstWish)
    print(line_break)
    print(twistList[random.randint(0, (len(twistList) - 1 ))])
    print(twistList[random.randint(0, (len(twistList) - 1 ))])
    print(twistList[random.randint(0, (len(twistList) - 1 ))])
    print()
    print(secondWish)
    print(line_break)
    print(twistList[random.randint(0, (len(twistList) - 1 ))])
    print(twistList[random.randint(0, (len(twistList) - 1 ))])
    print(twistList[random.randint(0, (len(twistList) - 1 ))])


create_suspense()

print("The genie for this game is " + genie_player + "!!!")
wishCounter = len(list_players)

input("Press enter to start the first round!")
os.system(clear_screen_command)


display_wishes()


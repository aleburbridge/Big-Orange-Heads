 # Text-based party game! 
# View the rules on the github page: ######

import os
import random
import time

def gain_250g():
    gold = humanplayer['gold']
    gold += 250
    humanplayer['gold'] = gold
gain250 = gain_250g

wishDict = {
    # gold wishes
    "Gain 250g": gain250,
    "Gain +100g for 3 turns (300g)": gain250,
    "Gain +75g for 5 turns (375g)": gain250,
    "Gold over time effects are worth +50%": gain250,
    "Gain 250g for each human with a big orange head": gain250,
    "Pick a human to receive 2x gold next gold wish (you can pick yourself)": gain250,

    # wishes about wishes
    "Gain two extra wishes": gain250,
    "Gain an extra wish option next turn": gain250,
    "Guarantee a gold wish option for the next three turns": gain250,

    # dice rolls
    "Roll a d12, gain 10x the gold shown": gain250,
    "Roll a d12. If over 5, +400g. If 5 or under, +100g over 4 turns": gain250,

    # wishes that improve odds
    "Human dice rolls have a 50\% chance to show a 12 (instead of 8%)": gain250,
    "Increase chance for legendary wishes to spawn (10% -> 20%)": gain250, # replace these with variables

    # items
    "Genie's lamp (Genie goes back in lamp and humans pick twist)": gain250,
    "Magic piggie bank (50g per turn for the rest of the game)": gain250,
    "Magic Wand (pick a big orange head to remove for 3 turns)": gain250
}

clear_screen_command = "cls" if input("Are you on Windows or Mac?\n" +
                                      "Enter W for Windows or anything else for Mac\n> ").strip().lower() == "w" else "clear"
os.system(clear_screen_command)

wishList = []
for key in wishDict.keys(): 
    wishList.append(key)

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


list_players = get_list_players()
number_of_players = len(list_players)
genie_player = list_players[(random.randint(0, (int(number_of_players) - 1)))]
dictionary_list_players = []

playerNumber = 1

for humanplayer in list_players:
    humanplayer = { 
        'name': humanplayer, 
        'gold': 0, 
        'big_orange_head': 'no', 
        'magic wand': 'no', 
        'wishes': 3,
        'player_number': playerNumber
        }
    playerNumber += 1
    dictionary_list_players.append(humanplayer)



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
wishesLeft = number_of_players * 3
winningGoldAmount = number_of_players * 500


def game_info(turn):
    print("gold - " + str(humanGoldTotal))
    print("items - ")
    print("Turn #" + str(turn))
    print("Wishes left - " + str(wishesLeft))
    player_number_check(turn)

def player_number_check(turn):
    for humanplayer in dictionary_list_players:
        if humanplayer['player_number'] == turn:
            print("Wisher: " + humanplayer['name'])


def display_wishes(turn):
    game_info(turn)
    create_suspense()


    print("~~ WISHES ~~")
    firstWish = ("1: " + wishList[random.randint(0, (len(wishList) - 1 ))])
    secondWish = ("2: " + wishList[random.randint(0, (len(wishList) - 1 ))])
    print(firstWish)
    print(line_break)
    print("a. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("b. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("c. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print()
    print(secondWish)
    print(line_break)
    print("a. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("b. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    print("c. " + twistList[random.randint(0, (len(twistList) - 1 ))])
    wisherResponse = input("\nWisher, type the number of your wish and press enter\n")
    if wisherResponse == "1":
        wishGranted = firstWish
    elif wisherResponse == "2":
        wishGranted = secondWish

    turn += 1

def startFirstRound():
    input("Press enter to start the first round!")
    os.system(clear_screen_command)

def startgame():
    displayIntro()
    print()
    create_suspense()
    print("The genie for this game is " + genie_player + "!!!")
    startFirstRound()
wishCounter = len(list_players)



startgame()
display_wishes(1)



import art
import blackjack
import config
# from replit import clear
from os import system

def play():
    print(art.logo)
    # player hands
    
    config.player = []
    config.computer = []
    # track each player's points
    config.points = {}
    
    blackjack.first_deal()
    #track points
    config.points["player"] = blackjack.player_total(config.player)
    config.points["computer"] = blackjack.player_total(config.computer)
    blackjack.game_rules()
    play_again = input("Would you like to play again? Type 'y' or 'n'.\n")
    system('clear')
    
    if play_again == "y":
        play()
    
play()
#!/usr/bin/env python3

import sys
import time
from roll_python_game.game.characters import Character







def run():
    chapters = [
        ["shady tavern", "midnight stables", "field"], # chapter 1 options
        ["swamp", "beach", "lake",], # chapter 2 options
        ["volcano", "wizard tower", "dark forest"], # chapter 3 options
        ["frozen mountain"], # chapter 4 options
    ]

    scenes = {
        "shady tavern": "Welcome to the shady tavern.\n",
        "midnight stables": "Welcome to the midnight stables.\n",
        "field": "Welcome to the field.\n",
        "swamp": "Welcome to the swamp.\n",
        "beach": "Welcome to the beach.\n",
        "lake": "Welcome to the lake.\n",
        "volcano": "Welcome to the volcano.\n",
        "wizard tower": "Welcome to the wizard tower.\n",
        "dark forest": "Welcome to the dark forest.\n",
        "frozen mountain": "Welcome to the frozen mountain.\n",
    }
    
    player = Character()
    print(f"Welcome to the game, {player.get_name()}.")
    try:
        for chapter in chapters: # make this be an imported function from a module
            print("Please select where to go next.\n")
            for option_num, option in enumerate(chapter):
                print(f"[{option_num + 1}]: {option}")
            print("\n")
            selection = input("---> ")
            count = 1
            # need to check that input != None
            while int(selection) not in range(1, len(chapter)+1): # input is bad
                print(f"Please select where to go next{','*count} again.\n")
                for option_num, option in enumerate(chapter):
                    print(f"[{option_num + 1}]: {option}")
                print("\n")
                selection = input("-" * count + "---> ")
                count += 1
            print(f"{scenes[chapter[int(selection) - 1]]}")
            time.sleep(1)
        print(f"Sorry, {player.get_name()}, you died from going so many places! Goodbye.\n")
        time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        sys.exit()




### From the interwebs ###
# player = Player()

# def run(start_at=None):
#     """Starts the game"""
#     player = Character() # load character
#     if not start_at:
#         scene = SCENES[0]
#     else:
#         scene = SCENES[start_at]
#     scene.init_player(player)
#     while 1:
#         new_scene = scene.run()
#         if new_scene != None:
#             scene = SCENES[new_scene]
#             scene.init_player(player)

if __name__ == "__main__":
    run()
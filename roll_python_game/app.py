#!/usr/bin/env python3

import sys
import time
from roll_python_game.game.characters import Character
from roll_python_game.game.enemy import Enemy
from roll_python_game.game.story import Story
from roll_python_game.game.act import Act
from roll_python_game.game.chapter import Chapter
from roll_python_game.game.scene import Scene





def run_chapter(chapter):
    #expects a chapter object
    print(chapter.get_title())
    print(chapter.get_description())
    time.sleep(0.5)
    for scene in chapter:
        scene.run_scene()

def show_chapter_options(chapter):
    for option_num, option in enumerate(chapter):
        print(f"[{option_num + 1}]: {option}")
    print("\n")

def clean_selection(selection):
    try:
        return int(selection)
    except ValueError as e:
        return 9999

def select_chapter(chapter_options, chapters):
    selection = clean_selection(input("---> "))
    count = 1
    while int(selection) not in range(1, len(chapter_options)+1): # input is bad
        print(f"Please select where to go next{','*count} again.\n")
        for option in chapter_options:
            print(option)
        selection = clean_selection(input("-" * count + "---> "))
        count += 1
    return chapters[selection]

def story_loop(story, scenes):
    for act in story: # make this be an imported function from a module
        print("Please select where to go next.\n")
        for option in act.get_options():
            print(option)
        # for option_num, option in enumerate(act.get_options()):
        #     print(f"[{option_num + 1}]: {option}")
        print("\n")
        selected_chapter = select_chapter(act.get_options(), act.get_chapters())
        #run_chapter(scenes[select_location(act.get_options(), scenes)])
        run_chapter(selected_chapter)

def run():
    player = Character()
    print(f"Welcome to the game, {player.get_name()}.")
    enemies = {
        "goblin": Enemy(
                        "Boblin", 
                        30,
                    ),
        "blob": Enemy(
                        "Blob", 
                        60,
                    ),
        "bugbear": Enemy(
                        "Bugbob", 
                        100,
                    )
    }

    scenes = {
        "shady tavern": [
            Scene(
                player,
                enemies["goblin"],
                "You approach the shady tavern.",
                "A goblin spots you and wants to kill you.",
                "After you effortlessly murder Boblin, you make your way inside."
                ),
            Scene(
                player,
                enemies["blob"],
                "You search shady tavern.",
                "The bartender is a blob and wants you out of his tavern.",
                "After you effortlessly murder Blob, you keep searching for the McGuffin."
                ),
            Scene(
                player,
                enemies["bugbear"],
                "You find the McGuffin and grab it. Now, time to leave.",
                "A murderous bugbear spots you on your way out.",
                "After you effortlessly murder Bugbob and make your way to the end of the chapter."
                ),
            ],
    }
    #finish adding the scenes
    scenes["midnight stables"] = scenes["shady tavern"]
    scenes["field"] = scenes["shady tavern"]
    scenes["swamp"] = scenes["shady tavern"]
    scenes["beach"] = scenes["shady tavern"]
    scenes["lake"] = scenes["shady tavern"]
    scenes["volcano"] = scenes["shady tavern"]
    scenes["wizard tower"] = scenes["shady tavern"]
    scenes["dark forest"] = scenes["shady tavern"]
    scenes["frozen mountain"] = scenes["shady tavern"]

    act1_chapters = {
        1: Chapter("shady tavern",
                   "shady tavern is shady",
                   scenes["shady tavern"]),
        2: Chapter("midnight stables",
                   "midnight stables desription",
                   scenes["midnight stables"]),
        3: Chapter("field",
                   "field desription",
                   scenes["field"]),
    }
    act2_chapters = {
        1: Chapter("swamp",
                   "swamp desription",
                   scenes["swamp"]),
        2: Chapter("beach",
                   "beach desription",
                   scenes["beach"]),
        3: Chapter("lake",
                   "lake desription",
                   scenes["lake"]),
    }
    act3_chapters = {
        1: Chapter("volcano",
                   "volcano desription",
                   scenes["volcano"]),
        2: Chapter("wizard tower",
                   "wizard tower desription",
                   scenes["wizard tower"]),
        3: Chapter("dark forest",
                   "dark forest desription",
                   scenes["dark forest"]),
    }
    act4_chapters = {
        1: Chapter("frozen mountain",
                   "frozen mountain desription",
                   scenes["frozen mountain"]),
    }
    # chapters = [
    #     ["shady tavern", "midnight stables", "field"], # chapter 1 options
    #     ["swamp", "beach", "lake"], # chapter 2 options
    #     ["volcano", "wizard tower", "dark forest"], # chapter 3 options
    #     ["frozen mountain"], # chapter 4 options
    # ]

    
    tale = Story([Act(act1_chapters), Act(act2_chapters), Act(act3_chapters), Act(act4_chapters)])
    # for chapter in tale:
    #     print(chapter.get_title(), end=" ")
    try:
        story_loop(tale, scenes)
        print(f"Sorry, {player.get_name()}, you died from going so many places! Goodbye.\n")
        time.sleep(0.5)
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
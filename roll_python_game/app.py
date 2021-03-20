#!/usr/bin/env python3

import sys
import time
from roll_python_game.game.characters import Character
from roll_python_game.game.enemy import Enemy
from roll_python_game.game.story import Story
from roll_python_game.game.act import Act
from roll_python_game.game.chapter import Chapter
from roll_python_game.game.scene import Scene

def load_story():
    # This will eventually pull from a database
    player = Character()
    print(f"\nWelcome to the game, {player.get_name()}.")
    print(player)
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
                "After you effortlessly murder Bugbob, you make your way to the end of the chapter."
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

    chapter_descriptions = { # actX_chapters can be generated more easily with this dict.
        "example location": ("title", "description"),
        "shady tavern": ("The Shady Tavern", "You spot a small tavern. It's shady.")
    }
    act1_chapters = {
        1: Chapter(chapter_descriptions["shady tavern"][0],
                   chapter_descriptions["shady tavern"][1],
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

    return Story([Act(act1_chapters), Act(act2_chapters),
                  Act(act3_chapters), Act(act4_chapters)])

def run():
    try:
        #playthrough
        for act in load_story(): act.run_act()
        #ending
        print(f"Sorry, {player.get_name()}, you died from going so many places! Goodbye.\n")
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("exiting")
        sys.exit()


if __name__ == "__main__":
    run()
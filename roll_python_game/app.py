#!/usr/bin/env python3

import sys
import time
from roll_python_game.game.characters import Character
from roll_python_game.game.goods import Weapon
from roll_python_game.game.goods import Armor
from roll_python_game.game.enemy import Enemy
from roll_python_game.game.story import Story
from roll_python_game.game.act import Act
from roll_python_game.game.chapter import Chapter
from roll_python_game.game.scene import Scene

# General Story:
# Setup: For centuries, a race of Asimar?, who could be spotted by their characteristic glowing eyes, have defended the people of World? from a race of dragons. The dragons just want to plunder the world and terrorize the people. A century ago, all of the Asimar were killed, leaving the dragons free reign of the world. Exhuming evil, the dragons bring rise to nasty beasties all over the lands. There is a dragon on the mountain nearby the protagonist's home village. It's been terrible.
# Act One: The protagonist is out on a coming of age hunt with friends. At midnight on the beginning of their 20th year, the protagonist's eyes begin to glow a brilliant white. Interrupting questioning from the friends is the hunted creature. After the hunt, they level up and feel slightly more apt, powerful even. One of the friends suggests talking to Bebop the elder to see if he knows why your eyes glow, just like the stories of the Asimar. Does anyone know where Bebop the elder is located? Yeah, he's in...*cut to next act where player makes choice of where to go.
# Act Two: The protagonist heads to meet the elder who reveals that they must be the long lost descendant of the Asimar. The last of the race. And what's more, is if you seek out [special amulet], you might be able to protect your village from the Ice Dragon.
# Act Three: The protagonist seeks out and acquires the McGuffin.
# Act Four: After some time of training, the protagonist is ready to ascend the mountain and slay the Ice Dragon.


# Chapter Layout
    # 
    # Chapter title:
    # Chapter intro: 
    # Scene 1 intro: 
    # Encounter 1 intro: 
    # Encounter 1 outro: 
    # Scene 1 outro: 
    # Scene 2 intro: 
    # Encounter 2 intro: 
    # Encounter 2 outro: 
    # Scene 2 outro: 
    # Scene 3 intro: 
    # Encounter 3 intro: 
    # Encounter 3 outro: 
    # Scene 3 outro: 
    # Chapter outro: 


def load_story():
    # This will eventually pull from a database
    #name="weapon", accuracy=1, damage=1, dmg_type="bludgeoning", level=0, class_tag="all"
    fist = Weapon("Fist", 0, 2, "bludgeoning", 0, "all"),
    weapons = {
        0: {
            "short sword": Weapon("Short Sword", 1, 4, "slashing", 0, "all"),
            "dagger": Weapon("Dagger", 3, 4, "piercing", 0, "rogue"),
            "fire wand": Weapon("Fire Wand", 1, 6, "fire", 0, "wizard"),
            "long sword": Weapon("Long Sword", 2, 5, "slashing", 0, "warrior"),
        },
        1: {
            "short sword": Weapon("Short Sword", 1, 4, "slashing", 1, "all"),
            "dagger": Weapon("Dagger", 3, 4, "piercing", 1, "rogue"),
            "poison dagger": Weapon("Poison Dagger", 4, 4, "poison", 1, "rogue"),
            "fire wand": Weapon("Fire Wand", 1, 6, "fire", 1, "wizard"),
            "long sword": Weapon("Long Sword", 2, 5, "slashing", 1, "warrior"),
        },
        2: {
            "short sword": Weapon("Short Sword", 1, 4, "slashing", 2, "all"),
            "dagger": Weapon("Dagger", 3, 4, "piercing", 2, "rogue"),
            "poison dagger": Weapon("Poison Dagger", 4, 4, "poison", 2, "rogue"),
            "fire wand": Weapon("Fire Wand", 1, 6, "fire", 2, "wizard"),
            "poison wand": Weapon("Poison Wand", 3, 5, "poison", 2, "wizard"),
            "long sword": Weapon("Long Sword", 2, 5, "slashing", 2, "warrior"),
            "ice sword": Weapon("Ice Sword", 2, 7, "piercing", 2, "warrior"),
        },
        3: {
            "ice dagger": Weapon("Ice Dagger", 4, 4, "ice", 3, "rogue"),
            "sharp dagger": Weapon("Sharp Dagger", 4, 7, "piercing", 3, "rogue"),
            "poison wand": Weapon("Poison Wand", 3, 5, "poison", 3, "wizard"),
            "fireball wand": Weapon("Fireball Wand", 6, 5, "fire", 3, "wizard"),
            "ice sword": Weapon("Ice Sword", 2, 7, "piercing", 3, "warrior"),
            "heavy sword": Weapon("Heavy Sword", 2, 10, "slashing", 3, "warrior"),
        },
    }
    armor = { #name="armor", ac=1, absorb=1, resistance="none", level=0, class_tag="all"
        0:{
            "bath robe": Armor(0, 0, "none", 0, "wizard"),
            "rags": Armor(1, 1, "none", 0, "rogue"),
            "overalls": Armor(2, 2, "none", 0, "warrior"),
        },
        1:{
            "robe": Armor(1, 1, "none", 1, "wizard"),
            "fitted clothes": Armor(3, 1, "none", 1, "rogue"),
            "leather armor": Armor(4, 4, "none", 1, "warrior"),
        },
    }
    items = {}
    enemies = {
        "goblin": Enemy("Boblin", 30),
        "blob": Enemy("Blob", 60),
        "bugbear": Enemy("Bugbob", 100)
    }

    player = Character()
    player.choose_class()
    print(f"\nWelcome to the game, {player.get_name()}.")
    print(player)

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
        "example location": ("title", "intro description", "outro description"),
        "shady tavern": ("The Shady Tavern", "You spot a small tavern. It's shady.", "Whew, glad to be done with the shady tavern!")
    }
    act1_chapters = {
        1: Chapter(chapter_descriptions["shady tavern"][0],
                   chapter_descriptions["shady tavern"][1],
                   chapter_descriptions["shady tavern"][2],
                   scenes["shady tavern"]),
        2: Chapter("midnight stables",
                   "midnight stables intro description",
                   "midnight stables outro description",
                   scenes["midnight stables"]),
        3: Chapter("field",
                   "field intro description",
                   "field outro description",
                   scenes["field"]),
    }
    act2_chapters = {
        1: Chapter("swamp",
                   "swamp intro description",
                   "swamp outro description",
                   scenes["swamp"]),
        2: Chapter("beach",
                   "beach intro description",
                   "swamp outro description",
                   scenes["beach"]),
        3: Chapter("lake",
                   "lake intro description",
                   "lake outro description",
                   scenes["lake"]),
    }
    act3_chapters = {
        1: Chapter("volcano",
                   "volcano intro description",
                   "volcano outro description",
                   scenes["volcano"]),
        2: Chapter("wizard tower",
                   "wizard tower intro description",
                   "wizard tower outro description",
                   scenes["wizard tower"]),
        3: Chapter("dark forest",
                   "dark forest intro description",
                   "dark forest outro description",
                   scenes["dark forest"]),
    }
    act4_chapters = {
        1: Chapter("frozen mountain",
                   "frozen mountain intro description",
                   "frozen mountain outro description",
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
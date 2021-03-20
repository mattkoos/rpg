#!/usr/bin/env python3

import time


def fight(hero, enemy):
    print(f"{enemy.get_name()} attacks {hero.get_name()}.\n")
    hero.add_xp(3)
    hero.update()
    # if hero loses, revert to save or quit [1]/[2]
    # lot of presented choices in this game, should probably make a function for it.





# Going to practice making character class to fight here and then copy text to other parts of project
#print("stuffy stuff")
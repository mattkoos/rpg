#!/usr/bin/env python3

import time
# from .characters import Character
# from .enemy import Enemy


def fight(hero, enemy):
    print(f"{enemy.get_name()} attacks {hero.get_name()}\n")
    time.sleep(0.5)
    hero.update()
    # if hero loses, revert to save or quit [1]/[2]
    # lot of presented choices in this game, should probably make a function for it.
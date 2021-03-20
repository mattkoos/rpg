#!/usr/bin/env python3

from .fight import fight

class Scene:

    def __init__(self, hero, enemy, intro_des, enemy_des, outro_des):
        self._hero = hero
        self._enemy = enemy
        self._intro_des = intro_des
        self._enemy_des = enemy_des
        self._outro_des = outro_des

    def run_scene(self):
        print(self._intro_des)
        input("_____________________________________________\n")
        print(self._enemy_des)
        input("_____________________________________________\n")
        fight(self._hero, self._enemy)
        print(self._outro_des)
        input("_____________________________________________\n")

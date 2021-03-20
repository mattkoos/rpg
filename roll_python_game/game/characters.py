#!/usr/bin/env python3


class Character():

    def __init__(self):
        self._name = ""
        self._progress = (1, 1) # playthrough, act, ?????chapter, scene
        self._level = 1
        self._xp = 0
        self._hp = 30
        self._ac = 10
        self._attack = 2
        self._weapon1 = "fists" # this will be a weapon object
        self._weapon2 = "" # this will be a weapon object

    def __str__(self):
        return (
            "************\n"
            f"* {self._name}\n"
            "*\n"
            f"* Level: {self._level}   Experience: {self._xp}\n"
            "*\n"
            f"* Armor: {self._ac}   Health: {self._hp}\n"
            "*\n"
            f"* Attack: {self._attack}   Weapons: {self._weapon1} {self._weapon2}\n"
            "************\n"
        )

    def get_name(self):
        if not self._name: # no name yet
            print("Hero name?")
            self._name = str(input("---> "))
        return self._name

    def add_xp(self, amount):
        self._xp += amount

    def get_xp(self):
        return self._xp

    def get_status(self):
        print(self) #should call the dunder str method
        # if player is ready to level up, state that here 

    def update(self):
        self.get_status()
        print("If the character needs to level up, this is where that happens.")
        

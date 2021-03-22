#!/usr/bin/env python3


from .choice import prompt_choice
from .goods import Weapon
from .goods import Armor

class Character:

    def __init__(self):
        self._name = ""
        self._progress = (1, 1) # playthrough, act, ?????chapter, scene
        self._level = 1
        self._xp = 0
        self._hp = 30
        self._ac = 10
        self._attack = 2 # adds to weapon accuracy AND weapon damage
        self._weapons = [None, None]
        self._armor = None
        self._items = []
        self._class = "nothing"

    def __str__(self):
        return (
            "************\n"
            f"* {self._name} the {self._class.title()}\n"
            "*\n"
            f"* Level: {self._level}   Experience: {self._xp}\n"
            "*\n"
            f"* Health: {self._hp}   Happiness: {'None'}\n"
            "*\n"
            f"* Armor Class: {self._ac}   Armor: {self._armor}\n"
            "*\n"
            f"* Attack: {self._attack}   Weapons: {self._weapons[0]}, {self._weapons[1]}\n"
            "************\n"
            "Inventory:\n"
            f"{str(self._weapons[0])*bool(self._weapons[0])}"
            f"{str(self._weapons[1])*bool(self._weapons[1])}"
            f"{str(self._armor)*bool(self._armor)}"
            f"{str(self._items)*bool(self._items)}"
        )

    def choose_class(self):
        choices = {
            1: "Wizard",
            2: "Rogue",
            3: "Warrior"
        }
        selection = prompt_choice(choices, "Please select what you want to be for the rest of your life.")
        self._class = choices[selection].lower()

    def add_weapon(self, weapon_class):
        new_weapon = weapon_class
        print(f"Cool! A {new_weapon}!\n")
        print(new_weapon.get_stats())
        if len(self._weapons) < 2: # can accomodate 2 weapons 
            self._weapons[len(self._weapons)] = weapon_class
            print(f"You can now use the {new_weapon}!")
        else:
            print("Current Weapons:")
            print(self._weapons[0].get_stats())
            print(self._weapons[1].get_stats())
            choices = {
                [1]: self._weapons[0],
                [2]: self._weapons[1],
                [3]: "Neither"
            }
            selection = prompt_choice(choices, "Please select weapon to replace.")
            if choices[selection] == "Neither":
                print("But who needs that? Not. You.")
            else:
                print(f"Goodbye, {choices[selection]}.")
                choices[selection] = new_weapon # Not really sure if this works....

    def add_armor(self, armor):
        # expects an armor instance
        new_armor = armor
        print(f"Cool! A {new_armor}!\n")
        print(new_armor.get_stats())
        if not self._armor: # can accomodate 2 weapons 
            self._armor = new_armor
            print(f"You're now wearing the {new_weapon}!")
        else:
            print("Current Armor:")
            print(self._armor.get_stats())
            choices = {
                [1]: "Replace current armor.",
                [2]: "Keep current armor."
            }
            selection = prompt_choice(choices, "Please select whether or not to replace.")
            if choices[selection] == "Keep current armor.":
                print("But who needs that? Not. You.")
            else:
                print(f"Goodbye, {self._armor}.")
                self._armor = new_armor

    def add_item(self, item):
        self._items.append(item)

    def get_name(self):
        while not self._name: # no name yet
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

    def check_level(self):
        next_level_xp = self._level * (self._level + 1)
        if self._xp >= next_level_xp: self.level_up()


    def level_up(self):
        # stats could be increased based on class
        print("Level Up!")
        self._level += 1

    def update(self):
        self.check_level()
        self.get_status()
        print("If the character needs to level up, this is where that happens.")
        

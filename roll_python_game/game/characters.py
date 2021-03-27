#!/usr/bin/env python3

import sys
from .choice import prompt_choice
from .goods import Weapon
from .goods import Armor
from roll_python_game.resources.console import console
from rich.panel import Panel
from rich.console import ConsoleOptions

class Character:

    def __init__(self):
        self._name = ""
        self._progress = (1, 1) # playthrough, act, ?????chapter, scene
        self._level = 1
        self._xp = 0
        self._next_lvl_xp = self.calc_next_lvl_xp(self._level)
        self._lvl_progress = self.calc_lvl_progress(self._level, self._xp)
        self._max_hp = 30
        self._current_hp = self._max_hp
        self._ac = 10
        self._absorb = 0 # increased from class/armor
        self._regen = 1 # health regen after each fight
        self._attack = 2 # adds to weapon accuracy AND weapon damage
        self._speed = 1 # initiative
        self._strength = 1 # intimidate *avoid
        self._stealth = 1 # sneak away *avoid
        self._charisma = 1 # persuade *avoid
        self._weapons = [Weapon("Fist", 0, 2, "bludgeoning", 0, "all"), Weapon("Fist", 0, 2, "bludgeoning", 0, "all")]
        self._armor = Armor("Nothing", 0, 0, [], 0, "all")
        self._items = ["pocket sand"]
        self._class_tag = "jobless"
        self.LEVEL_UP_DISPATCHER = { # need to be static vars
            1: (self.increase_stat, ["ac", 1]),
            2: (self.increase_stat, ["attack", 2]),
            3: (self.increase_stat, ["regen", 1]),
            4: (self._weapons[0].upgrade, None),
            5: (self._weapons[1].upgrade, None),
            6: (self._armor.upgrade, None),
            7: (self.new_equipment, None),
            8: (self.adjust_hp, [0.5]),
        }

    def __rich_console__(self, console: console, options: ConsoleOptions):
        yield f"[blue b]{self._name} the {self._class_tag.title()}[/blue b]\n"
        yield f"Level: [b]{self._level}[/b]   XP: [b]{self._xp}[/b]\n"
        yield f"{self._level}{'-'*self._lvl_progress}{' '*(20-self._lvl_progress)}{self._level + 1}\n"
        yield f"Health: [b]{self._current_hp}[/b]   Max Health: [b]{self._max_hp}[/b]\n"
        yield f"Armor Class: [b]{self._ac}[/b]   Armor: {self._armor}\n"
        yield f"Attack: [b]{self._attack}[/b]   Weapons: {self._weapons[0]}, {self._weapons[1]}\n"
        yield f"Speed: [b]{self._speed}[/b]   Stealth: [b]{self._stealth}[/b]\n"
        yield f"Strength: [b]{self._strength}[/b]   Charisma: [b]{self._charisma}[/b]\n"
        yield "\n"
        yield "[u]Inventory[/u]\n"
        yield f"{str(self._items)*bool(self._items)}\n"

    def get_sheet(self):
        console.print(Panel(self, border_style="blue"))

    # def __str__(self):
    #     return (
    #         "\n"
    #         "************\n"
    #         f"* {self._name} the {self._class_tag.title()}\n"
    #         "*\n"
    #         f"* Level: {self._level}   XP: {self._xp}\n"
    #         f"* {self._level}{'-'*self._lvl_progress}{' '*(20-self._lvl_progress)}{self._level + 1}\n"
    #         "*\n"
    #         f"* Health: {self._current_hp}   Max Health: {self._max_hp}\n"
    #         "*\n"
    #         f"* Armor Class: {self._ac}   Armor: {self._armor}\n"
    #         "*\n"
    #         f"* Attack: {self._attack}   Weapons: {self._weapons[0]}, {self._weapons[1]}\n"
    #         "*\n"
    #         f"* Speed: {self._speed}   Stealth: {self._stealth}\n"
    #         "*\n"
    #         f"* Strength: {self._strength}   Charisma: {self._charisma}\n"
    #         "************\n"
    #         "Inventory:\n"
    #         f"{str(self._items)*bool(self._items)}\n"
    #     )

    def get_name(self):
        return self._name

    def choose_class(self):
        choices = {
            1: "Wizard",
            2: "Rogue",
            3: "Warrior"
        }
        selection = prompt_choice(choices, "Please select what you want to be for the rest of your life.")
        self._class_tag = choices[selection].lower()
        print(f"Ahhh, {self._name} the {self._class_tag.title()}!")
        # self._level -= 1
        # self.level_up()
        # switch case for self._class_tag to adjust a few stats
        # or just lower level by one and then trigger level_up

    def new_equipment(self):
        print(f"New, level {self._level} equipment for {self._class_tag}.")

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

    
    def get_weapons(self, num):
        return self._weapons[num]

    def get_weapon1(self):
        return self._weapons[0]

    def get_weapon2(self):
        return self._weapons[1]

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

    def get_armor(self):
        return self._armor

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

    def get_name(self):
        while not self._name: # no name yet
            print("Hero name?")
            self._name = str(input("---> "))
        return self._name

    def add_xp(self, amount):
        self._xp += amount

    def get_xp(self):
        return self._xp

    def get_hp(self):
        return self._current_hp

    def get_max_hp(self):
        return self._max_hp

    def get_attack(self):
        return self._attack

    def get_ac(self):
        return self._ac

    def get_absorb(self):
        return self._absorb

    def get_speed(self):
        return self._speed

    def adjust_hp(self, amount):
        if 0 < amount < 1: # heals a portion of max_hp
            amount = int((self._max_hp * amount) + 0.5) # 0.5 makes int() round
        self._current_hp += amount
        self._current_hp = max(self._current_hp, 0)
        self._current_hp = min(self._current_hp, self._max_hp)

    def increase_stat(self, stat, amount): 
        # print(f"increase stat from {stat}...")
        # stat += amount
        # print(f"...to: {stat}")
        if stat == "max_hp":
            self._max_hp += amount
            self.adjust_hp(amount)
        elif stat == "speed":
            self._speed += amount
        elif stat == "stealth":
            self._stealth += amount
        elif stat == "strength":
            self._strength += amount
        elif stat == "charisma":
            self._charisma += amount
        elif stat == "ac":
            self._ac += amount
        elif stat == "attack":
            self._attack += amount
        elif stat == "absorb":
            self._absorb += amount

    def die(self):
        print(f"{self._name} has fallen, goodbye.")
        sys.exit()

    def calc_next_lvl_xp(self, level):
        if not level: return 0
        return 2 + (level * (level + 1))

    def calc_lvl_progress(self, level, xp):
        # returns number between 0 and 19 where 20 would happen at level up
        progress = (xp - self.calc_next_lvl_xp(level - 1)) / (self.calc_next_lvl_xp(level) - self.calc_next_lvl_xp(level - 1))
        return min(max(0, int(progress * 20)), 20)

    def check_level(self):
        self._lvl_progress = self.calc_lvl_progress(self._level, self._xp)
        self.get_sheet()
        if self._xp >= self.calc_next_lvl_xp(self._level): self.level_up()

    def level_up(self):
        print("Level Up!")
        self._level += 1
        ### automatic stat increase based on level
        if self._class_tag == "warrior": # meatier, get med acc, med dmg weapons
            self.increase_stat("max_hp", self._level * 2)
            # self.adjust_hp(self._level * 2)
            self.increase_stat("absorb", 3)
            self.increase_stat("attack", 2)
        elif self._class_tag == "rogue": # get high acc, med dmg weapons
            self.increase_stat("max_hp", int(self._level * 1.5))
            # self.adjust_hp(int(self._level * 1.5))
            self.increase_stat("absorb", 2)
            self.increase_stat("attack", 2)
        elif self._class_tag == "wizard": # get med acc, really high damage weapons
            self.increase_stat("max_hp", self._level)
            # self.adjust_hp(self._level)
            self.increase_stat("absorb", 1)
            self.increase_stat("attack", 1)
        else:
            print("Check level_up() for current class...")

        ### stat increase choice
        options = {
            1: "speed",
            2: "stealth",
            3: "strength",
            4: "charisma"
        }
        selection = prompt_choice(options, "Please select the attribute you would like to increase.")
        self.increase_stat(options[selection], 1)

        ### level up choice
        options = {
            1: "Increase AC by 1. (reduce chances of being hit)",
            2: "Increase Attack by 2. (increase chances of landing attack and damage)",
            3: "Increase Regeneration by 2. (increase amount healed between encounters)",
            4: f"Upgrade {self._weapons[0]}. (increases chances of landing attack and damage for the weapon)",
            5: f"Upgrade {self._weapons[1]}. (increases chances of landing attack and damage for the weapon)",
            6: "Upgrade armor. (reduce damage taken and chances of being hit with the armor)",
            7: "Get new weapon or armor.",
            8: "Heal 50% HP.",
        }
        selection = prompt_choice(options, "Please select level up improvement.")
        dispatch_function, args = self.LEVEL_UP_DISPATCHER[selection]
        if args:
            dispatch_function(*args)
        else:
            dispatch_function()
        self.check_level()

    def update(self):
        self.check_level() # This will trigger self.level_up()
        #self.get_status()
        

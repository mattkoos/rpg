#!/usr/bin/env python3

import time
from random import randrange
from .choice import prompt_choice
from roll_python_game.resources.console import console



dmg_styles = {
    "bludgeoning": "[#EABD01 italic]",
    "slashing": "[#D3320C italic]",
    "piercing": "[#7500FF italic]",
    "fire": "[#FF7000 italic]",
    "ice": "[#00C9FF italic]",
    "poison": "[#14AF15 italic]",
}



def roll_initiative(hero, enemy):
    hero_initiative = get_roll() + hero.get_speed()
    enemy_initiative = get_roll() + enemy.get_speed()
    console.print("[b]Who goes first?[/]")
    console.print(f"{hero.get_name()} rolls [b]{hero_initiative}[/], {enemy.get_name()} rolls [b]{enemy_initiative}[/]\n")
    return hero_initiative, enemy_initiative

def get_roll():
    return randrange(20) + 1

def attack(name, roll, accuracy, damage, dmg_type, # attacker stats
                ac, absorb, resistances): # defender stats
    # input are values from both attacker and target, returns damage amount
    console.print(f"[b]{name}'s[/b] attack roll: [b]{roll+accuracy}[/]")
    if roll+accuracy > ac:
        if dmg_type in resistances:
            return max((damage // 2) - absorb, 0)
        else:
            return max(damage - absorb, 0)
    else:
        console.print(f"[b]{name}[/b] [i]missed![/i]")
        return 0

def enemy_attack(hero, enemy):
    #enemy attack
    damage = attack(
        enemy.get_name(),get_roll(), enemy.get_accuracy(), enemy.get_damage(),
        enemy.get_dmg_type(), hero.get_ac(),
        hero.get_absorb() + hero.get_armor().get_absorb(),
        hero.get_armor().get_resistances()
    )
    if damage:
        hero.adjust_hp(-damage)
        console.print(f"[b]{enemy.get_name()}[/b] hit [b]{hero.get_name()}[/b] for {damage} {dmg_styles[enemy.get_dmg_type()]}{enemy.get_dmg_type()}[/] damage.")

def hero_attack(hero, enemy, attack_weapon):
    #hero attack
    damage = attack(
        hero.get_name(), get_roll(), hero.get_attack() + attack_weapon.get_accuracy(),
        hero.get_attack() + attack_weapon.get_damage(), attack_weapon.get_dmg_type(),
        enemy.get_ac(), enemy.get_absorb(), enemy.get_resistances()
    )
    if damage:
        enemy.adjust_hp(-damage)
        console.print(f"[b]{hero.get_name()}[/b] hit [b]{enemy.get_name()}[/b] for {damage} {dmg_styles[attack_weapon.get_dmg_type()]}{attack_weapon.get_dmg_type()}[/] damage.")

def fight(hero, enemy):
    choices = {
        1: f"Use {hero.get_weapon1()}.",
        2: f"Use {hero.get_weapon2()}.",
        3: f"Use {hero.get_weapon1()} repeatedly, until low health.",
        4: f"Use {hero.get_weapon2()} repeatedly, until low health.",
        #5: f"Use an item from: {hero.get_items()}.",
    }
    print(f"{enemy.get_name()} attacks {hero.get_name()}!\n")
    hero_initiative, enemy_initiative = roll_initiative(hero, enemy)
    repeat_selection = False
    if hero_initiative >= enemy_initiative:
        while 1: #hero goes first
            #weapon selection
            if not (repeat_selection and hero.get_hp() > (hero.get_max_hp() // 5)):
                selection = prompt_choice(choices, "Please select an action.")
                if selection in [3, 4]: # need to refactor this copied code
                    attack_weapon = hero.get_weapons(selection-3)
                    repeat_selection = True
                else:
                    attack_weapon = hero.get_weapons(selection-1)
            hero_attack(hero, enemy, attack_weapon)
            if not enemy.get_hp(): break
            enemy_attack(hero, enemy)
            if not hero.get_hp(): break
            print("\n")
    else:
        while 1: #enemy goes first
            enemy_attack(hero, enemy)
            if not hero.get_hp(): break
            #weapon selection
            if not (repeat_selection and hero.get_hp() > (hero.get_max_hp() // 5)):
                selection = prompt_choice(choices, "Please select an action.") 
                if selection in [3, 4]: # need to refactor this copied code
                    attack_weapon = hero.get_weapons(selection-3)
                    repeat_selection = True
                else:
                    attack_weapon = hero.get_weapons(selection-1)
            hero_attack(hero, enemy, attack_weapon)
            if not enemy.get_hp(): break
            print("\n")
    # who died?
    if not hero.get_hp():
        hero.die()
    else:
        hero.add_xp(enemy.get_xp())
        console.print(f"[b]{hero.get_name()}[/b] has killed [b]{enemy.get_name()}[/]!")
    hero.update()
    # if hero loses, revert to save or quit [1]/[2]
    # lot of presented choices in this game, should probably make a function for it.





# Going to practice making character class to fight here and then copy text to other parts of project
#print("stuffy stuff")
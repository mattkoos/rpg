#!/usr/bin/env python3

import random


# Do an ABC called Equipment that Weapon and Armor inherit from
class Weapon:

    WEAPON_COLORS = ['red', 'blue', 'silver', 'purple', 'yellow', 'gold', 'green', 'black', 'white']

    def __init__(self, name="weapon", accuracy=1, damage=1, dmg_type="bludgeoning", level=0, class_tag="all"):
        # possible dmg_types: "bludgeoning", "slashing", "piercing", "fire", "ice", "poison"
        # possible class_tags: "warrior", "wizard", "rogue"
        self._name = name
        self._accuracy = accuracy # base stat, updated by level
        self._damage = damage # base stat, updated by level
        self._dmg_type = dmg_type
        self._level = 0
        for level in range(level): self.upgrade()
        self._class_tag = class_tag
        self._color = random.choice(Weapon.WEAPON_COLORS)

    def __str__(self):
        return f"level {str(self._level)} {self._name}"

    def get_stats(self):
        return (
            "**********"
            f"* level {str(self._level)} {self._name}:"
            f"* accuracy: {str(self._accuracy)}   damage: {self._damage}"
            f"* damage type: {self._dmg_type}   color: {self._color}"
            "**********"
        )

    def upgrade(self):
        self._level += 1
        self._accuracy += 2
        self._damage += 1


class Armor:

    ARMOR_COLORS = ['red', 'blue', 'silver', 'purple', 'yellow', 'gold', 'green', 'black', 'white']

    def __init__(self, name="armor", ac=1, absorb=1, resistance="none", level=0, class_tag="all"):
        # possible dmg_types(for resistance): "bludgeoning", "slashing", "piercing", "fire", "ice", "poison", "all"
        # possible class_tags: "warrior", "wizard", "rogue"
        self._name = name
        self._ac = ac
        self._absorb = absorb
        self._resistance = resistance
        self._level = level
        self._class_tag = class_tag
        self._color = random.choice(Armor.ARMOR_COLORS)

    def __str__(self):
        return f"level {str(self._level)} {self._name}"

    def get_stats(self):
        return (
            "**********"
            f"* level {str(self._level)} {self._name}:"
            f"* ac: {str(self._ac)}   absorb: {self._abosrb}"
            f"* resistance: {self._resistance}   color: {self._color}"
            "**********"
        )

    def upgrade(self):
        self._level += 1
        self._ac += 1
        self._absorb += 1


class Item:

    def __init__(self):
        pass
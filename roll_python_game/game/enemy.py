#!/usr/bin/env python3


# This will eventually inherit from Characters ABC
class Enemy:

    def __init__(self, name, weight, hp, ac, absorb, accuracy, damage, dmg_type, speed, resistances, xp):
        self._name = name
        self._weight = weight
        self._hp = hp
        self._ac = ac
        self._absorb = absorb
        self._accuracy = accuracy
        self._damage = damage
        self._dmg_type = dmg_type
        self._speed = speed
        self._resistances = resistances
        self._xp = xp

    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight

    def get_hp(self):
        return self._hp

    def adjust_hp(self, amount):
        self._hp += amount
        self._hp = max(self._hp, 0)

    def get_ac(self):
        return self._ac

    def get_absorb(self):
        return self._absorb

    def get_resistances(self):
        return self._resistances

    def get_accuracy(self):
        return self._accuracy

    def get_damage(self):
        return self._damage

    def get_dmg_type(self):
        return self._dmg_type

    def get_speed(self):
        return self._speed

    def get_xp(self):
        return self._xp
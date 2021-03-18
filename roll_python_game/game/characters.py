#!/usr/bin/env python3

class Character():

    def __init__(self):
        self._name = ""

    def get_name(self):
        if not self._name: # no name yet
            self._name = str(input("Character name: "))
        print(self._name)

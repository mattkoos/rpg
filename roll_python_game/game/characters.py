#!/usr/bin/env python3

class Character():

    def __init__(self):
        self._name = ""
        self._progress = (1, 1, 1) # playthrough, chapter, scene

    def get_name(self):
        if not self._name: # no name yet
            print("Hero name?")
            self._name = str(input("---> "))
        return self._name

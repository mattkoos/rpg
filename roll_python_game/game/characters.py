#!/usr/bin/env python3

class Character():

    def __init__(self):
        self._name = ""
        self._progress = (1, 1) # playthrough, act, ?????chapter, scene
        self.level = 1

    def get_name(self):
        if not self._name: # no name yet
            print("Hero name?")
            self._name = str(input("---> "))
        return self._name

    def get_status(self):
        print(f"Here is the state of {self._name}.")
        # if player is ready to level up, state that here 

    def update(self):
        self.get_status()
        print("If the character needs to level up, this is where that happens.")
        

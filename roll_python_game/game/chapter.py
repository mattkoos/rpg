#!/usr/bin/env python3

class Chapter:

    def __init__(self, title, description, scenes):
        self._title = title
        self._description = description
        self._scenes = scenes # this should be a list of Scene() instances

    def __getitem__(self, index):
        # Here we can loop through the scenes of the chapter
        return self._scenes[index]

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description


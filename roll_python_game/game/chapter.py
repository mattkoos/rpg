#!/usr/bin/env python3


class Chapter:

    def __init__(self, title, intro_description, outro_description, scenes):
        self._title = title
        self._intro_description = intro_description
        self._outro_description = outro_description
        self._scenes = scenes # this should be a list of Scene() instances

    def get_title(self):
        return self._title

    def run_chapter(self):
        print(f"\n| {self._title} |\n")
        print(self._intro_description)
        for scene in self._scenes:scene.run_scene()
        print(self._outro_description)
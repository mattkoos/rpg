#!/usr/bin/env python3

from .choice import prompt_choice


class Act:

    def __init__(self, chapters):
        self._chapters = chapters # this should be a dictionary

    def get_chapter_options(self):
        # returns a dictionary for use with choice.choice()
        options = {}
        for key in self._chapters.keys():
            options[key] = self._chapters[key].get_title()
        return options

    def clean_selection(self, selection):
        try:
            return int(selection)
        except ValueError:
            return 9999

    def select_chapter(self):
        selection = prompt_choice(self.get_chapter_options(),
                           "Please select where to go next.")
        return self._chapters[selection]

    def run_act(self):
        self.select_chapter().run_chapter()
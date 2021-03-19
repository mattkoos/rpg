#!/usr/bin/env python3


class Act:

    def __init__(self, chapters):
        self._chapters = chapters # this should be a dictionary

    def get_chapters(self):
        return self._chapters

    def get_options(self):
        return [f"[{num}] {self._chapters[num].get_title()}" for num in sorted(self._chapters.keys())]
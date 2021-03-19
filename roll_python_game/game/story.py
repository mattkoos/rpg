#!/usr/bin/env python3


class Story:

    def __init__(self, acts=[]):
        self._acts = acts

    def __getitem__(self, index):
        return self._acts[index]


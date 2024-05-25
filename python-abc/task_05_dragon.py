#!/usr/bin/python3
"""
This module contain 2 class SwimMixin and FlyMixin
and a mix class Dragon
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

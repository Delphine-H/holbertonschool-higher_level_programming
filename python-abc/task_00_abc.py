#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal
    """

    @abstractmethod
    def sound(self):
        """Abstract method sound"""
        pass


class Dog(Animal):
    """
    class Dog that inherit Animal class
    """

    def sound(self):
        """Abstract method sound"""
        return "Bark"


class Cat(Animal):
    """
    class Cat that inherit Animal class
    """

    def sound(self):
        """ "Abstract method sound"""
        return "Meow"

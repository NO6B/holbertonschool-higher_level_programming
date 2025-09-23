#!/usr/bin/env python3
"""Animal Class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """dog class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """cat class"""
    def sound(self):
        return "Meow"

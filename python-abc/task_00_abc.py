#!/usr/bin/env python3
"""Animal Class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass


class Dog(Animal):
    """dog class"""
    def Sound(self):
        return "Bark"


class Cat(Animal):
    """cat class"""
    def Sound(self):
        return "Meow"

#!/usr/bin/env python3
"""2 function for serialize and deserialize"""
import pickle


class CustomObject:
    """customObjet class"""

    def __init__(self, name, age, is_student) -> None:
        """initialisation of attributes"""
        self.name = name
        self.age = age
        self. is_student = is_student

    def display(self):
        """print attributes"""
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize object in to file"""
        if not filename:
            return None
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserialize the content of filename"""
        if not filename:
            return None
        with open(filename, "rb") as f:
            obj = pickle.load(f)
            return obj

#!/usr/bin/env python3
import pickle


class CustomObject:

    def __init__(self, name, age, is_student) -> None:
        self.name = name
        self.age = age
        self. is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        if not filename:
            return None
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            return None
        with open(filename, "rb") as f:
            return pickle.load(f)

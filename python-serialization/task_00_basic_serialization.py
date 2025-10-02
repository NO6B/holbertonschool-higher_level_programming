#!/usr/bin/env python3
"""2 function for serialize and deserialize"""
import pickle


def serialize_and_save_to_file(data, filename):
    """serialize_and_save_to_file"""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """load_and_deserialize"""
    with open(filename, "rb") as f:
        return pickle.load(f)

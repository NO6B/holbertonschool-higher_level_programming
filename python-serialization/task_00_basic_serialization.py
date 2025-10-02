#!/usr/bin/env python3
"""2 function for serialize and deserialize"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize_and_save_to_file"""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """load_and_deserialize"""
    with open(filename, "r") as f:
        return json.load(f)

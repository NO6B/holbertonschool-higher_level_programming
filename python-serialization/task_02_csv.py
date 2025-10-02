#!/usr/bin/env python3
"""convert_csv_to_json function"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """function convert to json"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return True
    except FileNotFoundError:
        return False

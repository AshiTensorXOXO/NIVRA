import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().with_name("data.json")


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if "periods" not in data:
        data = {
            "academic_system": None,
            "periods": [
                {
                    "name": "Unassigned",
                    "subjects": data["subjects"],
                    "tasks": data["tasks"]
                }
            ]
        }
        save_data(data)

    return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
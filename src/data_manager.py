import json


def load_data():
    with open("src/data.json", "r") as file:
        data = json.load(file)

    return data


def save_data(subjects, tasks):
    data = {
        "subjects": subjects,
        "tasks": tasks
    }

    with open("src/data.json", "w") as file:
        json.dump(data, file, indent=4)
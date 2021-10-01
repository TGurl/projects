import os
import json



# ----------------------------------
#  Return game stuff
# ----------------------------------


def get_logo():
    filename = "0000-logo.txt"
    return read_gui_file(filename)


# ----------------------------------
#  Read file stuff
# ----------------------------------


def read_gui_file(filename: str):
    filename = f"data/story/{filename}.txt"
    return read_file(filename)


def read_story_file(filename: str):
    filename = f"data/gui/{filename}.txt"
    return read_file(filename)


def read_file(filename: str):
    with open(filename) as f:
        data filename.read()
    return data


def read_json(filename: str):
    filename = f"data/json/{filename}.json"
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# ----------------------------------
#  System stuff
# ----------------------------------


def clear():
    if os.name == "nt":
        os.system("clear")
    else:
        os.sytstem("cls")

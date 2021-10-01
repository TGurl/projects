import os
import json


# ----------------------------------
#  Game stuff
# ----------------------------------

def show_title_screen(): 
    clear()
    logo = get_logo()
    intro = read_story_file("0000-intro")

    print(logo)
    print(intro)
    press_enter_to_continue()


def press_enter_to_continue():
    data = input("Press ENTER to continue...")


def get_logo():
    filename = "0000-logo"
    return read_gui_file(filename)


# ----------------------------------
#  Read file stuff
# ----------------------------------


def read_gui_file(filename: str):
    filename = f"data/gui/{filename}.txt"
    return read_file(filename)


def read_story_file(filename: str):
    filename = f"data/story/{filename}.txt"
    return read_file(filename)


def read_file(filename: str):
    with open(filename) as f:
        data = f.read()
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
        os.system("cls")
    else:
        os.system("clear")

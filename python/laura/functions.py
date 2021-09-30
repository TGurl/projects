import os
import keyboard

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_terminal_size():
    columns, rows = os.get_terminal_size(0)
    return columns, rows


def get_logo():
    logo = read_gui('0000-logo.txt')
    return logo


def center(line: str):
    columns, rows = get_terminal_size()
    padding_left = int((columns - len(line)) / 2)
    line = padding_left * " " + line
    return line


def show_title_screen():
    clear()
    logo = get_logo()
    title_text = read_gui('0000-titlescreen.txt')
    logolines = ""
    titlelines = ""

    for line in logo:
        logolines += center(line) + "\n"

    for line in title_text:
        titlelines += center(line) + "\n"

    print(logolines)
    print(titlelines)
    keyboard.wait('enter')


def read_gui(filename: str):
    filename=f'data/gui/{filename}'
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data


def read_chapter(filename: str):
    filename = f'data/story/{filename}'
    with open(filename, 'r') as f:
        data = f.read()
    return data

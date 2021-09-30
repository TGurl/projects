#!/usr/bin/env python
from tkinter import *
from PIL import Image, ImageTk
from functions import *


def main():
    frame_width = 1280

    root = Tk()
    #root.geometry('+%d+%d' % (10, 10))

    header = Frame(root, width=frame_width, height=150, bg="white")
    header.grid(columnspan=3, rowspan=2, row=0)

    main_content = Frame(root, width=frame_width, height=400, bg="#20bebe")
    main_content.grid(columnspan=3, rowspan=2, row=4, padx=0, pady=0)

    display_logo('assets/logoxl.png', 0, 0)

    chapter = read_chapter('0000-intro.txt')
    display_textbox(chapter, 4, 0, root)

    root.mainloop()


if __name__ == '__main__':
    main()

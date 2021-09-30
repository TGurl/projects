from tkinter import *
from PIL import Image, ImageTk


def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg='white')
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2,
                   sticky=NW, padx=0, pady=0)


def display_textbox(content, ro, col, root):
    text_box = Text(root, height=23, width=50,
                    padx=10, pady=10, font=('Cantarell', 18))
    text_box.insert(1.0, content)
    #text_box.tag_configure("center", justify="center")
    #text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=col, row=ro, sticky=NW, padx=12, pady=12)


def read_chapter(filename: str):
    filename = f'data/story/{filename}'
    with open(filename, 'r') as f:
        data = f.read()
    return data

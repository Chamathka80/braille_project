
from tkinter import *

import tkinter as tk

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x300")
window.configure(bg="#D5CFCF")

canvas = Canvas(
    window,
    bg="#D5CFCF",
    height=300,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    9.0,
    10.0,
    689.0,
    290.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    62.0,
    36.0,
    237.0,
    270.375,
    fill="#C4C4C4",
    outline="")

canvas.create_text(
    62.0,
    20.0,
    anchor="nw",
    text="Preview",
    fill="#848484",
    font=("Archivo Regular", 10 * -1)
)

button_image_upload = PhotoImage(
    file=relative_to_assets("upload_button.png"))
upload_button = Button(
    image=button_image_upload,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: upload_file(),
    relief="flat"
)
upload_button.place(
    x=350.0,
    y=114.0,
    width=168.0,
    height=72.0
)


def upload_file():
    global img
    f_types = [("Jpg Files", "*.jpg")]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((170, 230))  # new width & height
    img = ImageTk.PhotoImage(img_resized)
    b2 = tk.Button(window, image=img)  # using Button
    b2.grid(row=1, column=1)
    b2.place(
        x=62.0,
        y=36.0,
    )
    # file_path = filename
    # print(filename)
    # --------------
    # return filename


# file_path = upload_file()
# ---------------------------------------------------------------------
canvas.create_text(
    400.0,
    100.0,
    anchor="nw",
    text="file_path",
    fill="#111",
    font=("Archivo Regular", 10 * -1),
)
button_image_close = PhotoImage(
    file=relative_to_assets("close_button.png"))
close_button = Button(
    image=button_image_close,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
close_button.place(
    x=650.0,
    y=20.0,
    width=20.0,
    height=20.0
)


def nextPage():
    window.destroy()
    import page2
    # import Preprocessing_image


button_image_next = PhotoImage(
    file=relative_to_assets("next_button.png"))
next_button = Button(
    image=button_image_next,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
next_button.place(
    x=388.0,
    y=199.0,
    width=98.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()

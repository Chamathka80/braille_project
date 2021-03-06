# import the necessary files & libraries
from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

global im_th

# functions

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# navigating to the next page
def nextPage():
    window.destroy()
    import page3

# navigating to the home page
def homePage():
    window.destroy()
    import page0


window = Tk()
window.title(
    'Construction of Restoration System for Old Books Written in Sinhala Braille')

window.geometry("700x300")
window.configure(bg="#D5CFCF")


canvas = Canvas(
    window,
    bg="#D5CFCF",
    height=300,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_rectangle(9.0, 10.0, 689.0, 290.0, fill="#FFFFFF", outline="")

button_image_close = PhotoImage(file=relative_to_assets("close_button.png"))
close_button = Button(
    image=button_image_close,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat",
)
close_button.place(x=650.0, y=20.0, width=20.0, height=20.0)


button_image_home = PhotoImage(file=relative_to_assets("home_button.png"))
home_button = Button(
    image=button_image_home,
    borderwidth=0,
    highlightthickness=0,
    command=homePage,
    relief="flat",
)
home_button.place(x=650.0, y=48.0, width=20.0, height=20.0)

button_image_detect = PhotoImage(file=relative_to_assets("detect_button.png"))
detect_button = Button(
    image=button_image_detect,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("detect_button clicked"),
    relief="flat",
)
detect_button.place(x=312.0, y=110.0, width=238.0, height=40.0)


button_image_translate = PhotoImage(
    file=relative_to_assets("translate_button.png"))
translate_button = Button(
    image=button_image_translate,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat",
)
translate_button.place(x=341.0, y=159.0, width=179.0, height=35.0)


img = Image.open("assets/thresholded_img/thresholded_image.jpg")
img_resized = img.resize((170, 230))  # new width & height
photo = ImageTk.PhotoImage(img_resized)
imglabel = Label(image=photo)
imglabel.place(
    x=47.0,
    y=36.0
)

canvas.create_rectangle(47.0, 35.625, 222.0, 270.0, fill="#C4C4C4", outline="")

canvas.create_text(
    47.0,
    20.0,
    anchor="nw",
    text="Preview",
    fill="#848484",
    font=("Archivo Regular", 10 * -1),
)
window.resizable(False, False)
window.mainloop()

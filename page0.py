# import the necessary files & libraries
from tkinter import *
from pathlib import Path


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# functions

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# navigating to the next page
def nextPage():
    window.destroy()
    import page1


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

canvas.create_text(
    590.0,
    260.0,
    anchor="nw",
    text="Team Debuggers",
    fill="#848484",
    font=("Archivo Regular", 10 * -1)
)

button_image_start = PhotoImage(
    file=relative_to_assets("start_button.png"))
start_button = Button(
    image=button_image_start,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
start_button.place(
    x=265.0,
    y=114.0,
    width=168.0,
    height=72.0
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
window.resizable(False, False)
window.mainloop()

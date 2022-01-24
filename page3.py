# import the necessary files & libraries
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# functions
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

canvas.create_rectangle(174.0, 36.0, 349.0, 270.375,
                        fill="#C4C4C4", outline="")

canvas.create_text(
    174.0,
    20.0,
    anchor="nw",
    text="Preview",
    fill="#848484",
    font=("Archivo Regular", 10 * -1),
)

button_image_save = PhotoImage(file=relative_to_assets("save_button.png"))
save_button = Button(
    image=button_image_save,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("save_button clicked"),
    relief="flat",
)
save_button.place(x=385.0, y=195.0, width=114.0, height=42.0)

window.resizable(False, False)
window.mainloop()

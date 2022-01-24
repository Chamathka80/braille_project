# import the necessary files & libraries
from tkinter import *
from pathlib import Path
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

import cv2
import numpy as np
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# functions

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 1. function to save the preprocessed image
def file_save():
    cv2.imwrite('assets/New Folder/test.jpg', im_th)

# 2. perform preprocessing steps
def preprocess_img(file_path):
    global im_th 

    # importing the image
    image = cv2.imread(file_path)

    # creating dimensions to resize the image
    scale_percent = 20 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resizing the image to the given scale percentage
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    # converting the image into gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #   kernal 
    kernel = np.ones((1,1), np.uint8)

    # dialation and erosion
    img_dilation = cv2.dilate(gray, kernel, iterations=1)
    img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

    # thresholding the image
    th, im_th = cv2.threshold(img_erosion, 130, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite("assets/New folder/thresholded_image.jpg", im_th)

    # Find Canny edges
    edged = cv2.Canny(im_th, 0, 255)
    # cv2.waitKey(0)

    # Finding Contours
    contours, hierarchy = cv2.findContours(edged,
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    # Draw the contours on the original image
    cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

# 3. uploading the selected image
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

    preprocess_img(filename)

# navigating to the next page
def nextPage():
    window.destroy()
    import page2


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

from PIL import Image
import os
import glob
directory = "D:\Educational Files\RUSL\Group Project\System\data\images\sinhala_braille_dataset_16002000 - Copy"
directories = [x[0] for x in os.walk(directory)]
size = (600, 600)

for d in directories:
    images = glob.glob(f'{d}/*.jpg')
    for image in images:
        im = Image.open(rf"{image}")
        im = im.resize(size)
        im.save(image)
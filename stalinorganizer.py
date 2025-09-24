import sys
import math
import colorsys
import os
from PIL import Image

def myexcepthook(type, value, traceback, oldhook=sys.excepthook):
    oldhook(type, value, traceback)
    input("Press RETURN. ")

sys.excepthook = myexcepthook
    
def get_main_color(file):
    img = Image.open(file)
    colors = img.getcolors(1000000) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

file = input("Enter file path  \n")
file = file.replace('"', '')
color = get_main_color(file)
r, g, b = color[:3]
hsv_color = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
h, s, v = hsv_color[:3]
h = h * 360
s = s * 100
v = v * 100
if (h < 11) & (s >= 20) & (v >= 20):
    print("passed, comrade")
else:
    print("send him to gulag")
    os.remove(file)
print(color)
print(hsv_color)
input("EXIT")
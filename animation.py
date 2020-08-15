import sys
from PIL import Image
import os
import time
from colored import fg, bg, attr
import random
from pyfiglet import Figlet
import sys

# pass the image as command line argument


# resize the image
def maker(img):
    width, height = img.size
    aspect_ratio = height/width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

# replace each pixel with a character from array
    chars = [" ","S","#","&","@","$","%","*","!",":"," "]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    print(ascii_image)
    return
count = 1  
n = input("Press Enter:")  
while True:
    if count > 24:
        count = 1        
    img = Image.open(sys.argv[1]+"/f" + str(count)+".png")
    color = [ "dark_orange","grey_93","green_4"]
    if count in range(1 , 9):
        colour_name = color[0]
    elif count in range(9 , 17):
        colour_name = color[1]
    else:
        colour_name = color[2]    
    print("%s%s"% (fg(colour_name),attr('bold')))
    f = Figlet(font= "pagga")
    maker(img)
    print(f.renderText('         HAPPY            \nINDEPENDENCE DAY'),end="")
    f = Figlet(font= "digital")
    print(f.renderText('             PROUDLY INDIAN'),end="")


    time.sleep(0.07)
    os.system("clear")
    count += 1

# write to a text file.
with open("ascii_image.txt", "w") as f:
 f.write(ascii_image)

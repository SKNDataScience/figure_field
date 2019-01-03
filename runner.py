from PIL import Image
import random
img = Image.open("logo.png")

width, height = img.size

white_counter = 0
nonwhite_counter = 0
for x in range(width):
    for y in range(height):
        pixel_color = img.getpixel((x, y))
        if pixel_color == (255, 255, 255, 255):
            white_counter += 1
        else:
            nonwhite_counter += 1
total_pixels = white_counter + nonwhite_counter
print("The precise ratio of the figures field to the field of the whole image is " +str(100*nonwhite_counter/total_pixels)+"%")

white_counter = 0
nonwhite_counter = 0
for i in range(10000):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    pixel_color = img.getpixel((x, y))
    if pixel_color == (255, 255, 255, 255):
        white_counter += 1
    else:
        nonwhite_counter += 1
    img.putpixel((x, y), (255, 0, 0, 255))
total_pixels = white_counter + nonwhite_counter
print("The estimated ratio of the figures field to the field of the whole image is " +str(100*nonwhite_counter/total_pixels)+"%")
img.save("dotted_logo.png")

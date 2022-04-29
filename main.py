# from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from apng import APNG
import cv2
from PIL import Image

files = []
flag = ""


# Gets the location of a picture from a linear array
def get_loc(pixel_loc, w):
    temp_height = 0
    temp = pixel_loc
    while temp > w:
        temp = temp - w
        temp_height = temp_height + 1
    return temp, temp_height


# Loads the animated png file
og_file = APNG.open("result.apng")

# Get each frame and save it as an individual png
for i, (png, control) in enumerate(og_file.frames):
    png.save("{i}.png".format(i=i))

# Loads each frame into an array (and also makes sure they're there
files = ["{i}.png".format(i=i) for i in range(38)]
for pic in files:
    print("Grabbing: " + pic.title())
# Compare each png to stock image
stock_image = Image.open("ostrich.jpg")
width, height = stock_image.size
stock_pixel = Image.frombytes("RGB", (width, height), stock_image.tobytes())
stock_pixels = list(stock_pixel.getdata())

for i in range(len(files)):
    test_image = Image.open(files[i].title())
    test_pixel = Image.frombytes("RGB", (width, height), test_image.tobytes())
    test_pixels = list(test_pixel.getdata())
    pix_loc = []
    dif_pixels = []
    for pix in range(len(test_pixels)):
        if stock_pixels[pix] != test_pixels[pix]:
            pix_loc.append(get_loc(pix, width))
            dif_pixels.append(test_pixels[pix])
    print(f"{dif_pixels} at: {pix_loc} of: {files[i].title()}")
print(f"Length: {len(files)}")

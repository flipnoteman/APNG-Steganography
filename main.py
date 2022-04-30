# cv2
import Cryptodome
from Cryptodome.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from PIL import Image
from apng import APNG

files = []
flag = ""


# Gets the location of a picture from a linear distance array
def get_loc(pixel_loc, w):
    temp_height = 0
    temp = pixel_loc
    while temp > w:
        temp = temp - w
        temp_height = temp_height + 1
    # Returns a Tuple (width, height)
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

# Iterates through each file and finds every pixel that's different
# from the original, prints out the pixel's RGB value, and it's (x, y) location in the image
for i in range(len(files)):
    test_image = Image.open(files[i].title())
    test_pixel = Image.frombytes("RGB", (width, height), test_image.tobytes())
    test_pixels = list(test_pixel.getdata())
    pix_locs_xy = []
    pix_locs_array = []
    dif_pixels = []
    for pix in range(len(test_pixels)):
        if stock_pixels[pix] != test_pixels[pix]:
            pix_locs_array.append(pix)
            pix_locs_xy.append(get_loc(pix, width))
            dif_pixels.append(test_pixels[pix])

    print(f"{dif_pixels} at: {pix_locs_xy} of: {files[i].title()}")

    pixel = stock_image.getpixel((get_loc()))

    # bad_byte = (dif_pixels[0])
    # orig_pix = stock_pixels[pix_locs_array[0]]
    # orig_pix_z = orig_pix[2]
    # unicode_flag = b2l(bytes(bad_byte)) / orig_pix_z
    # print(chr(int(unicode_flag)))

    # unicode_flag = b2l(test_pixels[pix_locs_array[0]])/stock_pixels[pix_locs_array[0]][2]
    # print(unicode_flag)
print(f"Length: {len(files)}")

import PIL.Image
import string
from tkinter.filedialog import askopenfilename

imgg =askopenfilename()
img = PIL.Image.open(imgg)
ascii_char = string.punctuation
new_width = 100

def resizeimg(img, new_width=100):
    width, height = img.size
    ratio = height / width
    new_height = int((new_width * ratio) / 2)
    resized_image = img.resize((new_width, new_height))
    return resized_image
def gray_scale(img):
    grayscale = img.convert("L")
    return grayscale
def pixel_ascii(img):
    pixels = img.getdata()
    ch = "".join([ascii_char[pixel//20] for pixel in pixels])
    return ch

new_image = pixel_ascii(gray_scale(resizeimg(img)))
pc = len(new_image)
ascii_image = "\n".join(new_image[i:(i+new_width)] for i in range(0, pc, new_width))
print(ascii_image)

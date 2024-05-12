# this script creates 1:1 images from strings in text.txt (separated by newlines) and images in the images/ directory. good for tierlists :p

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

default_size = 300
in_text_file = 'text.txt'
in_img_dir = 'images'
out_dir = 'output'

fg_color = "white"
bg_color = "black"
font = "NotoSans-Regular.ttf"

text = [] # read from text.txt later

# create dirs
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

if not os.path.exists(in_img_dir):
    os.makedirs(in_img_dir)

if not os.path.exists(in_text_file):
    with open(in_text_file, 'w') as file:
        file.write('')

if (input(f"clear {out_dir}? (Y/n): ").strip() or 'y') == 'y':
    for item in os.listdir(out_dir):
        os.remove(f"{out_dir}/{item}")

size = int(input(f"enter size of the images (def {default_size}): ").strip() or default_size)

# read the text file and store each line in a tuple, omit whitespace lines
with open('text.txt', 'r') as file:
    for line in file:
        if line.strip() != '':
            text += (line.strip(),)

print(f"got these from text.txt:\n{text}")

if (input(f"sort text? (y/N): ").strip() or 'n') == 'y':
    text = sorted(text)
    print(f"sorted text:\n{text}")

def create_image(size, bg, message, font, fg):
    print(f"creating image with size {size} and message {message}")

    W, H = size
    img = Image.new('RGB', size, bg)

    draw = ImageDraw.Draw(img)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fg)

    return img

def resize_image(size, image):
    print(f"resizing image {image} to {size}x{size}")

    img = Image.open(image)
    
    # crop to 1:1
    w, h = img.size
    if w > h:
        img = img.crop(((w-h)/2, 0, (w+h)/2, h))
    else:
        img = img.crop((0, (h-w)/2, w, (h+w)/2))

    # resize
    img = img.resize((size, size))

    return img

i = 0

for item in text:
    # img = create_image((size,size), bg_color, item, ImageFont.load_default(size/3), fg_color)
    img = create_image((size,size), bg_color, item, ImageFont.truetype(font, size//3), fg_color)    
    img.save(f"{out_dir}/{i}.png") 
    i+=1

for item in os.listdir(in_img_dir):
    img = resize_image(size, f"{in_img_dir}/{item}")
    img.save(f"{out_dir}/{i}.png")
    i+=1

print(f"done, created {i} images")



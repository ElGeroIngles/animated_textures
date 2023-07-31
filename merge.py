from PIL import Image
import os

# folder path
dir_path = r'C:\Users\germa\Documents\datapack\frames'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

width = 256
height = 11264

img  = Image.new( mode = "RGB", size = (width, height))

y = 0

int(count)

for x in range(44):
    print(x)
    try:
        frame = Image.open(f"{dir_path}/frame{x}.jpg")
        img.paste(frame, (0, y))
        y += 256
    except:
        print("error")

img.save("frames_merged.png")


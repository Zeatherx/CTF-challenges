from PIL import Image
import numpy as np

width = 552
height = 45

with open("White_RGBA.txt", "r") as f:
    data = list(map(int, f.read().split(",")))

rgba = np.array(data, dtype=np.uint8)

#replace all 254 → 1
rgba[rgba == 254] = 1

rgba = rgba.reshape((height, width, 4))

img = Image.fromarray(rgba, "RGBA")
img.save("output.png")

print("Saved as output.png")

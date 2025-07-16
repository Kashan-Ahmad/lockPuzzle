from PIL import Image
import numpy as np

def rgb_to_565(r, g, b):
    # Convert 8-bit RGB to 5-6-5 format
    R = (r >> 3) & 0x1F
    G = (g >> 2) & 0x3F
    B = (b >> 3) & 0x1F
    return (R << 11) | (G << 5) | B

# 1) Load your ghost image
image = Image.open("candy.png").convert("RGB")


# 2) Resize to 20x20 using nearest-neighbor
image_resized = image.resize((20, 20), Image.NEAREST)

# 3) Convert to NumPy array and then to 5-6-5 hex
pixels = np.array(image_resized)
hex_array = []

for row in pixels:
    row_hex = []
    for (r, g, b) in row:
        val_565 = rgb_to_565(r, g, b)
        row_hex.append(f"0x{val_565:04X}")
    hex_array.append(row_hex)

# 4) Print the data row by row
for row in hex_array:
    print(",".join(row) + ",")

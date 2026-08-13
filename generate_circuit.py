#!/usr/bin/env python3
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create a high-quality Qiskit-style circuit diagram using PIL
width, height = 1000, 400
img = Image.new('RGB', (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Try to load a nice font
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    label_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
except:
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        title_font = label_font = small_font = ImageFont.load_default()

# Draw the qubit line and labels
qubit_y = 200
x_start = 120
x_end = 900

# Draw qubit label "q:"
draw.text((20, qubit_y - 20), "q:", font=label_font, fill=(0, 0, 0))

# Draw qubit wire (horizontal line)
draw.line([(x_start, qubit_y), (x_end, qubit_y)], fill=(0, 0, 0), width=2)

# H gate
h_x = 250
gate_size = 50
# Draw H gate box
draw.rectangle([h_x - gate_size//2, qubit_y - gate_size//2,
                h_x + gate_size//2, qubit_y + gate_size//2],
               outline=(0, 0, 0), width=3, fill=(200, 200, 255))
# Draw H label
draw.text((h_x - 12, qubit_y - 14), "H", font=label_font, fill=(0, 0, 0))

# T gate
t_x = 450
# Draw T gate box
draw.rectangle([t_x - gate_size//2, qubit_y - gate_size//2,
                t_x + gate_size//2, qubit_y + gate_size//2],
               outline=(0, 0, 0), width=3, fill=(200, 200, 255))
# Draw T label
draw.text((t_x - 12, qubit_y - 14), "T", font=label_font, fill=(0, 0, 0))

# Draw connection lines from wire to gates
draw.line([(x_start, qubit_y), (h_x, qubit_y)], fill=(0, 0, 0), width=2)
draw.line([(h_x, qubit_y), (t_x, qubit_y)], fill=(0, 0, 0), width=2)
draw.line([(t_x, qubit_y), (x_end, qubit_y)], fill=(0, 0, 0), width=2)

# Add small vertical lines for gate connections
for gate_x in [h_x, t_x]:
    draw.line([(gate_x, qubit_y - gate_size//2), (gate_x, qubit_y)],
              fill=(0, 0, 0), width=2)
    draw.line([(gate_x, qubit_y), (gate_x, qubit_y + gate_size//2)],
              fill=(0, 0, 0), width=2)

# Draw title at top
draw.text((width//2 - 150, 30), "Quantum Circuit", font=title_font, fill=(0, 0, 0))

# Draw description at bottom
desc_y = height - 60
draw.text((20, desc_y), "Circuit order: H applied first, then T", font=small_font, fill=(64, 64, 64))
draw.text((20, desc_y + 35), "Matrix multiplication: T·H (reversed order)", font=small_font, fill=(64, 64, 64))

# Save the image
img.save('images/circuit_order.png')
print("High-quality circuit diagram saved to images/circuit_order.png")
print(f"Image size: {width}x{height} pixels")

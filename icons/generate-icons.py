# Run this once to generate icons: python3 generate-icons.py
# Requires: pip install Pillow
from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Gradient-like background using rounded rect
    margin = int(size * 0.08)
    draw.rounded_rectangle([margin, margin, size-margin, size-margin],
                            radius=int(size*0.22), fill='#6C5CE7')
    # Inner lighter circle
    c = size // 2
    r = int(size * 0.28)
    draw.ellipse([c-r, c-r, c+r, c+r], fill='#A29BFE')
    # Money emoji-like symbol
    font_size = int(size * 0.42)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()
    text = '₹'
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size-tw)//2 - bbox[0], (size-th)//2 - bbox[1]), text, fill='white', font=font)
    img.save(f'icon-{size}.png')
    print(f'Created icon-{size}.png')

make_icon(192)
make_icon(512)

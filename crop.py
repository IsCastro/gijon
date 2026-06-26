import sys
from PIL import Image, ImageOps, ImageEnhance

# Uso: crop.py <src> <x1> <y1> <x2> <y2> <out.jpg>
src, x1, y1, x2, y2, out = sys.argv[1:7]
x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

BG = (14, 17, 22)
im = Image.open(src).convert('RGBA')
bg = Image.new('RGBA', im.size, BG + (255,))
im = Image.alpha_composite(bg, im).convert('RGB')

im = im.crop((x1, y1, x2, y2))

# cuadrado (rellena si hiciera falta)
side = max(im.size)
sq = Image.new('RGB', (side, side), BG)
sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
sq = sq.resize((440, 440), Image.LANCZOS)

# blanco y negro con un punto de contraste, al estilo de la tarjeta
g = ImageOps.grayscale(sq)
g = ImageEnhance.Contrast(g).enhance(1.08)
g.convert('RGB').save(out, quality=88)
print('saved', out)

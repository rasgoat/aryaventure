from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new('RGB', (W, H), '#000000')
draw = ImageDraw.Draw(img)

# Try to use system fonts, fallback to default
def get_font(size, bold=False):
    candidates = [
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/SFCompact.ttf',
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf',
    ]
    for f in candidates:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, size)
            except:
                continue
    return ImageFont.load_default()

font_title = get_font(72, bold=True)
font_sub = get_font(24)
font_url = get_font(18)

# Wordmark centered
text = 'ARYAVENTURE'
bbox = draw.textbbox((0, 0), text, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) / 2, H / 2 - 60), text, fill='#ffffff', font=font_title)

# Subtitle
sub = 'Premium Digital Agency'
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
sw = bbox2[2] - bbox2[0]
draw.text(((W - sw) / 2, H / 2 + 30), sub, fill=(255, 255, 255, 102), font=font_sub)

# URL bottom right
draw.text((W - 220, H - 56), 'aryaventure.com', fill='#c8ff00', font=font_url)

out = os.path.join(os.path.dirname(__file__), 'og-image.png')
img.save(out, 'PNG')
print(f'Saved {out} ({W}x{H})')

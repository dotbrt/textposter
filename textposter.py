from PIL import Image, ImageDraw, ImageFont

size = (1080, 1080)
image = Image.new(mode="RGBA", size=size, color='hsl(60,100%,50%)')
draw = ImageDraw.Draw(image)
text = 'Marshmallow bear claw cake sesame snaps jelly-o jelly powder. Ice cream pastry tiramisu. at cake dessert fruitcake cotton candy gummi bears cookie.'
font = ImageFont.truetype('Provicali.otf', 30)
draw.text((80,150), text[:40], fill=(0,0,0,255), font=font)
print(font.getsize(text))
image.show()

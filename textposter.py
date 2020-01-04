from PIL import Image, ImageDraw, ImageFont

size = (1080, 1080)
image = Image.new(mode="RGBA", size=size, color='hsl(60,100%,50%)')
draw = ImageDraw.Draw(image)
input = 'Pastry jelly oat cake caramels tart chupa chups. Danish donut sweet roll lemon drops toffee cheesecake pie jelly beans. Cake apple pie caramels jelly gummies carrot cake toffee bear claw. Sesame snaps dragée lemon drops oat cake sweet roll bear claw caramels carrot cake sesame snaps. Halvah candy tart tiramisu toffee pastry jelly-o. Croissant gingerbread marshmallow.'
n = 40


"""
Breaks line after number of character specified in n if the char is _space_ 
"""
def break_line(n, text):
    if '\n' in text:
        pass
    else:
        while n < len(text):
            if text[n].isspace():
                text = text[:n] + '\n' + text[n+1:]
                #text2 = '\n'.join([text[i:i+n] for i in range(0, len(text), n)])
                n+=40
            elif text[n] == '\n':
                n+=40
            else:
                n+=1
    return text
text = break_line(n, input)
font = ImageFont.truetype('Provicali.otf', 30)
draw.multiline_text((80,150), text, fill=(0,0,0,255), font=font, spacing=20)
image.show()
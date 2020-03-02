from PIL import Image, ImageDraw, ImageFont
import json


#Input data
data_json = 'data.json' # Data source

'''Image configuration'''
#image = Image.open('sample4.jpg') #Image source
res = (1080,1080) # Picture size
source_file = input("Provide file name: ")
try:
    image = Image.open(source_file)
except FileNotFoundError:
    image = Image.new(mode="RGBA", size=res, color='hsl(60,100%,50%)')

'''Font configuration'''
set_font = "fonts/Bellarina.otf"
font = ImageFont.truetype(set_font, 35)
spacing = 20 #letter spacing
line_length = 40 # Max length of a line
text_color = (0,0,0,255)

#Generate single color background


# Loads data source
def load_json(data_json):
    """Loads JSON file"""
    with open(data_json) as f:
        d = json.load(f)
    return d

#Break line
def break_line(n, text):
    """Breaks line after number of character specified in n if the char is _space_"""
    if '\n' in text[:n]:
        pass
    else:
        while n < len(text):
            if text[n].isspace():
                text = text[:n] + '\n' + text[n+1:]
                n+=line_length
            elif text[n] == '\n':
                n+=line_length
            else:
                n+=1
    return text

#Position Y in 50% of height
def calc_pos_y(image, text):
    """Positions text in the center of Y based on Image class size """
    return int((image.size[1]/2)-(text_size[1]/2))

def calc_pos_x(image):
    """Vertically positions text in the image"""
    return int(round(image.size[0] * 0.15))

'''data input configuration'''
data = load_json(data_json)['post']['msg'] # Load data from datasource

draw = ImageDraw.Draw(image) # draw a loaded image
text = break_line(line_length, data)
text_size = draw.multiline_textsize(text, font=font, spacing=spacing)
pos_y = calc_pos_y(image, text)
pos_z = calc_pos_x(image)
draw.multiline_text((150,pos_y), text, fill=text_color, font=font, spacing=spacing)

image.show()
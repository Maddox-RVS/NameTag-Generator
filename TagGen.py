from PIL import Image, ImageDraw, ImageFont, ImageColor
import os 

currentDir = cwd = os.getcwd()
fontName = "Freshman"

font = ImageFont.truetype(currentDir + "\\Fonts\\" + fontName + ".ttf")
background = Image.new("RGB", [800, 400], 0)
nameTag = ImageDraw.Draw(background)
nameTag.multiline_text(xy=(10, 60), 
             text="This is a test", 
             fill=(123, 100, 210), 
             font=font, anchor="mb", 
             spacing=4, 
             align="left", 
             direction=None, 
             features=None, 
             language=None, 
             stroke_width=0, 
             stroke_fill=None, 
             embedded_color=False)
background.show()
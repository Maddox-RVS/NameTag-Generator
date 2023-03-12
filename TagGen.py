from PIL import Image, ImageDraw, ImageFont, ImageColor
import os 

currentDir :str = os.getcwd()
fontName :str = "Freshman"

name :str = "Myles"
initial :str = "S"
title :str = "Programmer / Drive Team"
teamNumber :str = "3173"
nameFontSize :int = 140
titleFontSize :int = 70
horizontalLineSideSpacing :int = 100
yellow = (252, 179, 21)

#Configure name font
nameFont = ImageFont.truetype(currentDir + "\\Fonts\\" + fontName + ".ttf", nameFontSize)

#Configure title font
titleFont = ImageFont.truetype(currentDir + "\\Fonts\\" + fontName + ".ttf", titleFontSize)

#Configure background
background = Image.open(currentDir + "\\Backgrounds\\igknighters_pin.png");
backgroundWidth = background.getbbox().__getitem__(2)
backgroundHeight = background.getbbox().__getitem__(3)


# Draw name
nameTag = ImageDraw.Draw(background)
nameBounds = nameTag.textbbox(xy=(0, 0), 
                        text=name + " " + initial + ".", 
                        font=nameFont)
nameBoundsWidth = nameBounds.__getitem__(2)
nameBoundsHeight = nameBounds.__getitem__(3)
nameTag.text(xy=((backgroundWidth/2) - nameBoundsWidth/2, (backgroundHeight/2) - nameBoundsHeight - 20), 
             text=name + " " + initial + ".", 
             fill=yellow, 
             font=nameFont,
             align="left", 
             direction=None, 
             features=None, 
             language=None, 
             stroke_width=0, 
             stroke_fill=None, 
             embedded_color=False)

#Draw long horizontal line underneath name
nameTag.line(xy=[(horizontalLineSideSpacing, backgroundHeight/2), 
                  (backgroundWidth-horizontalLineSideSpacing, backgroundHeight/2)], 
                   fill=yellow, 
                   width=6)

# Draw number
teamNumberTag = ImageDraw.Draw(background)
numberBounds = teamNumberTag.textbbox(xy=(0, 0), 
                        text=teamNumber,
                        font=titleFont)
numberBoundsWidth = numberBounds.__getitem__(2)
numberBoundsHeight = numberBounds.__getitem__(3)
teamNumberTag.text(xy=((backgroundWidth - horizontalLineSideSpacing) - numberBoundsWidth, (backgroundHeight/2) + 20), 
             text=teamNumber, 
             fill=yellow, 
             font=titleFont,
             align="left", 
             direction=None, 
             features=None, 
             language=None, 
             stroke_width=0, 
             stroke_fill=None, 
             embedded_color=False)

#Draw long vertical line between title and number
numberBoundsX = (backgroundWidth - horizontalLineSideSpacing) - numberBoundsWidth
nameTag.line(xy=[((numberBoundsX - 4) - 20, backgroundHeight/2 + 20), 
                  ((numberBoundsX - 4) - 20, backgroundHeight/2 + 85)], 
                   fill=yellow, 
                   width=4)
                   
# Draw title
numberBoundsX = (backgroundWidth - horizontalLineSideSpacing) - numberBoundsWidth
titleTag = ImageDraw.Draw(background)
titleBounds = titleTag.textbbox(xy=(0, 0), 
                        text=title,
                        font=titleFont)
titleBoundsWidth = titleBounds.__getitem__(2)
titleBoundsHeight = titleBounds.__getitem__(3)
titleTag.text(xy=((numberBoundsX - titleBoundsWidth) - 40, (backgroundHeight/2) + 20), 
             text=title, 
             fill=yellow, 
             font=titleFont,
             align="left", 
             direction=None, 
             features=None, 
             language=None, 
             stroke_width=0, 
             stroke_fill=None, 
             embedded_color=False)

print(nameBounds)
print(titleBounds)
print(numberBounds)

background.show()
image = background
image.save(currentDir + "\\Output\\test.png", format="png")
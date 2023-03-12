from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back, Style
import keyboard
import time
import os 

currentDir :str = os.getcwd()
listPath :str = ""
backgroundPath :str = ""
fontPath :str = ""

def chooseList():
    tagListsPath = currentDir + "\\Tag Lists"
    lists = []
    for filename in os.listdir(tagListsPath):
        if filename.endswith('.txt'):
            fileNameWithoutExt = os.path.splitext(filename)[0]
            lists.append(fileNameWithoutExt)
    
    selectedIndex = 0
    menuReprint = True
    while True:
        if menuReprint == True:
            os.system('cls')
            print(Fore.YELLOW + "Use the arrow keys to navigate.\n\nChoose a name list:\n" + Style.RESET_ALL)
            for i in range(lists.__len__()):
                if (i == selectedIndex):
                    print(Back.WHITE + "[" + str(i) + "] " + lists[i] + Style.RESET_ALL)
                else:
                    print("[" + str(i) + "] " + lists[i])
        if keyboard.is_pressed('down'):
            if (selectedIndex != lists.__len__() - 1):
                selectedIndex += 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('up'):
            if (selectedIndex != 0):
                selectedIndex -= 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('enter'):
            os.system('cls')
            time.sleep(1)
            return currentDir + "\\Tag Lists\\" + lists[selectedIndex] + ".txt"
        else:
            menuReprint = False


def chooseBackground():
    backgroundPaths = currentDir + "\\Backgrounds"
    backgrounds = []
    for filename in os.listdir(backgroundPaths):
        if filename.endswith('.png'):
            fileNameWithoutExt = os.path.splitext(filename)[0]
            backgrounds.append(fileNameWithoutExt)
    
    selectedIndex = 0
    menuReprint = True
    while True:
        if menuReprint == True:
            os.system('cls')
            print(Fore.YELLOW + "Use the arrow keys to navigate.\n\nChoose a background image:\n" + Style.RESET_ALL)
            for i in range(backgrounds.__len__()):
                if (i == selectedIndex):
                    print(Back.WHITE + "[" + str(i) + "] " + backgrounds[i] + Style.RESET_ALL)
                else:
                    print("[" + str(i) + "] " + backgrounds[i])
        if keyboard.is_pressed('down'):
            if (selectedIndex != backgrounds.__len__() - 1):
                selectedIndex += 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('up'):
            if (selectedIndex != 0):
                selectedIndex -= 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('enter'):
            os.system('cls')
            time.sleep(1)
            return currentDir + "\\Backgrounds\\" + backgrounds[selectedIndex] + ".png"
        else:
            menuReprint = False


def chooseFontPath():
    fontPath = currentDir + "\\Fonts"
    fonts = []
    for filename in os.listdir(fontPath):
        if filename.endswith('.ttf'):
            fileNameWithoutExt = os.path.splitext(filename)[0]
            fonts.append(fileNameWithoutExt)
    
    selectedIndex = 0
    menuReprint = True
    while True:
        if menuReprint == True:
            os.system('cls')
            print(Fore.YELLOW + "Use the arrow keys to navigate.\n\nChoose a font:\n" + Style.RESET_ALL)
            for i in range(fonts.__len__()):
                if (i == selectedIndex):
                    print(Back.WHITE + "[" + str(i) + "] " + fonts[i] + Style.RESET_ALL)
                else:
                    print("[" + str(i) + "] " + fonts[i])
        if keyboard.is_pressed('down'):
            if (selectedIndex != fonts.__len__() - 1):
                selectedIndex += 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('up'):
            if (selectedIndex != 0):
                selectedIndex -= 1
                menuReprint = True
                time.sleep(0.15)
        elif keyboard.is_pressed('enter'):
            os.system('cls')
            time.sleep(1)
            return currentDir + "\\Fonts\\" + fonts[selectedIndex] + ".ttf"
        else:
            menuReprint = False

listPath = chooseList()
backgroundPath = chooseBackground()
fontPath = chooseFontPath()

names = []
initials = []
titles = []

with open(listPath, 'r') as file:
    for line in file:
        currLine = line.strip()
        words = currLine.split(",")
        names.append(words[0])
        initials.append(words[1])
        titles.append(words[2])

for person in range(names.__len__()):
    name :str = names[person]
    initial :str = initials[person]
    title :str = titles[person]
    space :str = "   "
    teamNumber :str = "3173"
    nameFontSize :int = 140
    titleFontSize :int = 70
    horizontalLineSideSpacing :int = 100
    yellow = (252, 179, 21)

    if (title.__len__() > 12):
        lettersOver = title.__len__() - 12
        titleFontSize -= lettersOver * 2

    if (name.__len__() > 7):
        lettersOver = name.__len__() - 7
        nameFontSize -= lettersOver * 5

    #Configure name font
    nameFont = ImageFont.truetype(fontPath, nameFontSize)

    #Configure title font
    titleFont = ImageFont.truetype(fontPath, titleFontSize)

    #Configure background
    background = Image.open(backgroundPath);
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
                    
    # Draw title and number
    titleTag = ImageDraw.Draw(background)
    titleBounds = titleTag.textbbox(xy=(0, 0), 
                            text=title,
                            font=titleFont)
    titleBoundsWidth = titleBounds.__getitem__(2)
    titleBoundsHeight = titleBounds.__getitem__(3)
    teamNumberTag = ImageDraw.Draw(background)
    numberBounds = teamNumberTag.textbbox(xy=(0, 0), 
                            text=teamNumber,
                            font=titleFont)
    numberBoundsWidth = numberBounds.__getitem__(2)
    numberBoundsHeight = numberBounds.__getitem__(3)
    spaceStr = ImageDraw.Draw(background)
    spaceBounds = spaceStr.textbbox(xy=(0, 0),
                                    text=space,
                                    font=titleFont)
    spaceWidth = spaceBounds.__getitem__(2)
    spaceHeight = spaceBounds.__getitem__(3)

    titleNumberWidth = titleBoundsWidth + spaceWidth + numberBoundsWidth 

    titleTag.text(xy=((backgroundWidth/2) - ((titleNumberWidth + spaceWidth)/2), (backgroundHeight/2) + 20), 
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

    teamNumberTag.text(xy=(((backgroundWidth/2) - ((titleNumberWidth + spaceWidth)/2)) + spaceWidth + titleNumberWidth - numberBoundsWidth, (backgroundHeight/2) + 20), 
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
    nameTag.line(xy=[(((backgroundWidth/2) - ((titleNumberWidth + spaceWidth)/2)) + titleBoundsWidth + spaceWidth, backgroundHeight/2 + 20), 
                    (((backgroundWidth/2) - ((titleNumberWidth + spaceWidth)/2)) + titleBoundsWidth + spaceWidth, backgroundHeight/2 + titleBoundsHeight + 25)], 
                    fill=yellow, 
                    width=4)

    image = background
    image.save(currentDir + "\\Output\\" + str(names[person]) + ".png", format="png")
    print("Saved " + names[person] + " to " + currentDir + "/Output")
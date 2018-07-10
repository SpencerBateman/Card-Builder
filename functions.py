from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import math
import yaml

config = yaml.load(open('data/config.yaml'))

# Takes in the card position in the printed list of cards and returns its
# coords for the printable page
def getCardPrintPosition(cardNumber):
    baseXShift = 120
    baseYShift = 70
    coords = (0,0)
    if cardNumber % 9 == 0:
        coords = (baseXShift + 0, baseYShift + 0)
    if cardNumber % 9 == 1:
        coords = (baseXShift + 755, baseYShift + 0)
    if cardNumber % 9 == 2:
        coords = (baseXShift + 1510, baseYShift + 0)
    if cardNumber % 9 == 3:
        coords = (baseXShift + 0, baseYShift + 1050)
    if cardNumber % 9 == 4:
        coords = (baseXShift + 755, baseYShift + 1050)
    if cardNumber % 9 == 5:
        coords = (baseXShift + 1510,baseYShift + 1050)
    if cardNumber % 9 == 6:
        coords = (baseXShift + 0, baseYShift + 2100)
    if cardNumber % 9 == 7:
        coords = (baseXShift + 755, baseYShift + 2100)
    if cardNumber % 9 == 8:
        coords = (baseXShift + 1510, baseYShift + 2100)
    return coords

def getCardFrameandColor(type):
    title_color = (255,255,255)
    if (type == config['equipment']):
        cardframe = Image.open('resources/cardframes/' + config['equipmentPath'])
        card_text_color = (0,0,0)
    if (type == config['villain']):
        cardframe = Image.open('resources/cardframes/' + config['villainPath'])
        title_color = (192,22,28)
        card_text_color = (0,0,0)
    if (type == config['superpower']):
        cardframe = Image.open('resources/cardframes/' + config['superpowerPath'])
        title_color = (240,130,33)
        card_text_color = (0,0,0)
    if (type == config['hero']):
        cardframe = Image.open('resources/cardframes/' + config['heroPath'])
        title_color = (0,174,239)
        card_text_color = (0,0,0)
    if (type == config['location']):
        cardframe = Image.open('resources/cardframes/' + config['locationPath'])
        title_color = (244,15,144)
        card_text_color = (0,0,0)
    if (type == config['supervillain']):
        cardframe = Image.open('resources/cardframes/' + config['supervillainPath'])
        # cardframe = Image.open('resources/cardframes/supervillain1.png')
        title_color = (192,22,28)
        card_text_color = (255,255,255)
    if (type == config['superlocation']):
        cardframe = Image.open('resources/cardframes/superlocation.png')
        title_color = (244,15,144)
        card_text_color = (255,255,255)
    if (type == config['superequipment']):
        cardframe = Image.open('resources/cardframes/superequipment.png')
        card_text_color = (255,255,255)
    return [title_color, card_text_color, cardframe]

## Takes in all of the nessesary info for the card and then returns an image
def makeCard(name, cost, type, text, vp, image):
    # background = Image.open('resources/blank2.png')
    background = Image.open('resources/blank.png')
    cardColorInfo = getCardFrameandColor(type)

    title = Image.new('RGBA',(800, 100), (255,255,255,0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype("resources/fonts/Compacta-Bold-Italic.otf", 60)
    draw.text((50, 30), name, cardColorInfo[0], font=font)

    lines = text.split('<br>')

    text = Image.new('RGBA',(800, 300), (255,255,255,0))
    text_applied = ImageDraw.Draw(text)

    linecounter = 1
    for line in lines:
        if line[:3] == '<b>':
            line = line[3:-4]
            font = ImageFont.truetype("resources/fonts/TradeGothicLTStd-Bold.otf", 26)
        else:
            for ch in ['<c>']:
                if ch in line:
                    line = line.replace(ch,',')
            font = ImageFont.truetype("resources/fonts/TradeGothicLTStd.otf", 26)
        text_applied.text((40, (linecounter * 34) - 15 ), line, cardColorInfo[1], font=font)
        linecounter = linecounter + 1

    ## Add Cost
    cost = Image.open('resources/costs/' + cost.strip() + '.png')

    ## Add Victory Points
    vp = Image.open('resources/vps/' + vp.strip() + '.png')

    ## Define card art
    picture = Image.open('data/' + config['imagepath'] + '/' + image.strip()).convert("RGBA")
    baseheight = 600
    hpercent = (baseheight / float(picture.size[1]))
    wsize = int((float(picture.size[0]) * float(hpercent)))
    picture = picture.resize((wsize, baseheight), Image.ANTIALIAS)

    # Assemble the image
    background.paste(picture, (375 - picture.width / 2, 105), picture)
    background.paste(cardColorInfo[2], (0,0), cardColorInfo[2])
    background.paste(cost, (0,0), cost)
    background.paste(vp, (0,0), vp)
    background.paste(title, (0,0), title)
    background.paste(text, (0,720), text)
    return background

def getPrintPages(cards):
    number_of_cards = len(cards)
    number_of_pages = math.ceil(number_of_cards / 9.0)
    pages = []

    i = 0
    while i < number_of_pages:
        pages.append(Image.new('RGBA',(2550, 3300), (255,255,255,0)))
        i = i + 1

    j = 0
    for card in cards:
        pages[int(math.floor(j / 9.0))].paste(card, getCardPrintPosition(j), card)
        j = j + 1

    # for page in pages:
        # page.show()

    return pages


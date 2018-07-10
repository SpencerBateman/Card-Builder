from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import progressbar
import sys
import yaml
import os
from functions import getCardPrintPosition, makeCard, getPrintPages

config = yaml.load(open('config.yaml'))

# number_of_rows_printed = config['rowsToPrint']

row_number = 0
list_of_cards = []
print 'building cards'

spreadsheet = open(config['pathToCSV']);
spreadsheet = spreadsheet.readlines()

## Remove header
spreadsheet.pop(config['startPrintLine'] - 2)
linesToPrint = []
if config['range']:
    for card in config['cardsToPrint']:
        linesToPrint.append(spreadsheet[int(card)])
else:
    linesToPrint = spreadsheet

bar = progressbar.ProgressBar(maxval=len(linesToPrint), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

for line in linesToPrint:

    # Split the values at the comma
    line_array = line.split(',')

    count_of_card = int(line_array[1])

    ## Program in duplicate cards
    while (count_of_card != 0):
        card = makeCard(line_array[0], line_array[4], line_array[2], line_array[3], line_array[5], line_array[6])
        list_of_cards.append(card)
        count_of_card = count_of_card - 1

    ## update the row number
    row_number = row_number + 1

    ## update progress bar
    bar.update(row_number)

## end the progress bar so it doesn't crash
bar.finish()

pages = getPrintPages(list_of_cards)
i = 0
print 'writing to disk'
secondBar = progressbar.ProgressBar(maxval=len(pages), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
secondBar.start()
for page in pages:
    if not os.path.exists(config['outputDir']):
        os.makedirs(config['outputDir'])
    page.save(config['outputDir'] + '/' + str(i) + '.png')
    i = i + 1
    # page.show()
    secondBar.update(i)
secondBar.finish()

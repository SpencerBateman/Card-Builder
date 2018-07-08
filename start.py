from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from functions import getCardPrintPosition, makeCard, getPrintPages
import csv
import progressbar
import sys

# number_of_rows_printed = 74
number_of_rows_printed = 2
bar = progressbar.ProgressBar(maxval=number_of_rows_printed, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

__path__ = 'avengers/print-t.csv'

list_of_cards = []

row_number = 0
list_of_cards = []
print 'building cards'
with open(__path__) as f:
    for line in f:
        if line[:9] != 'Card Name':
            ## Make sure we only print the correct number of unique cards
            if number_of_rows_printed > row_number:

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

            ## Once every row has been printed the loop ends
            else:
                ## end the progress bar so it doesn't crash
                bar.finish()
                # print list_of_cards

                pages = getPrintPages(list_of_cards)
                i = 0
                print 'writing to disk'
                secondBar = progressbar.ProgressBar(maxval=len(pages), \
                    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
                secondBar.start()
                for page in pages:
                    page.save('deck/' + str(i) + '.png')
                    i = i + 1
                    secondBar.update(i)
                secondBar.finish()
                break;

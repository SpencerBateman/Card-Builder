# DC Deckbuilding Card Builder

## TODO
  * Make the program not crash with the progress bar but work.
  * Make it only print out a set number of cards.
  * Fix off by one card layout error

## config.yaml
  * pathToCSV -- releative path the to comma separated values file for the deck.
  * villain: 'Villain'
  * villainPath: 'villainframe.png'
* hero: 'Hero'
* heroPath: 'heroframe.png'
* superpower: 'Super Power'
* superpowerPath: 'spframe.png'
* equipment: 'Equipment'
* equipmentPath: 'eqframe.png'
* location: 'Location'
* locationPath: 'locframe.png'
* supervillain: 'Super Villain'
* supervillainPath: 'supervillain.png'
* superlocation: 'Super Location'
* superequipment: 'Super Equipment'
* imagepath: 'images/'
  * rowsToPrint -- The total numbers of rows in your csv that leads to printing a full deck. Is set this way so that you can have extra rows at the end of your spreadsheet for calcualting stats about your deck.
  * startPrintLine -- The line of the csv that the deck starts at. This way you have remove header column information depending on your spreadsheet.
  * range -- Set to True if you want to print a subset of cards defined in the cardsToPrint list, false if you want to print the whole deck.
  * outputDir -- the directory that the card sheets will be output to
  * cardsToPrint -- a collection of cell numbers of individual cards that will be printed if the range boolean is set to true.

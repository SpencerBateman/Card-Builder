# DC Deckbuilding Card Builder
```
root/
|
|- data/
|  |
|  |- images/
|  |- spreadsheet.csv
|  |- config.yaml
|
|- resources/
|  |
|  |- cardframes/
|  |- costs/
|  |- fonts/
|  |- vps/
|  |- blank.png
|  |- blank2.png
|
|- README.md
|- functions.py
|- start.py

```

## config.yaml
  * pathToCSV -- releative path the to comma separated values file for the deck.
  * villain: -- What you are naming villains in this game
  * villainPath: path to the cardframe for villain type in the card frames folder
  * hero: -- What you are naming hero's in this game
  * heroPath: -- path to the cardframe for hero type in the card frames folder
  * superpower: What you are naming super powers in this game
  * superpowerPath: path to the cardframe for super power type in the card frames folder
  * equipment: What you are naming equipment in this game
  * equipmentPath: path to the cardframe for the equipment type in the card frames folder
  * location: What you are naming locations in this game
  * locationPath: path to the cardframe for location type in the card frames folder
  * supervillain: What you are naming super villains in this game
  * supervillainPath: path to the cardframe for super villain type in the card frames folder
  * superlocation: This is a test variable not to be worried about right now
  * superequipment: This is a test variable not to be worried about right now
  * imagepath: the folder that images are stored in, this folder has  to be in a data folder.
  * rowsToPrint -- The total numbers of rows in your csv that leads to printing a full deck. Is set this way so that you can have extra rows at the end of your spreadsheet for calcualting stats about your deck.
  * startPrintLine -- The line of the csv that the deck starts at. This way you have remove header column information depending on your spreadsheet.
  * range -- Set to True if you want to print a subset of cards defined in the cardsToPrint list, false if you want to print the whole deck.
  * outputDir -- the directory that the card sheets will be output to
  * cardsToPrint -- a collection of cell numbers of individual cards that will be printed if the range boolean is set to true.

## Format of Spreadsheet
| Card Name | Count | Card Type | Card Text        | Cost | Victory Points |  Image Link  |
| --------- | ----- | --------- | ---------------- | ---- | -------------- | ------------ |
| Batarang  | 4     | Equipment | \<b>+2 Power\<b> | 2    | 1              | batarang.png |


## TODO
  * Higher res cards at proper size.
  * Handle bold and unbold on the same line
  * Fix typographic line spacing to be more like original cards.
  * Back card title with black backing title text
  * Add set button customization
  * Add ip button customization

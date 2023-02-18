## Changes for 2.4

For this release, many thanks goes to Cyrille Bougot for his work.
* Table navigation fixed in MS Word
* Introduce new commands following changes in NVDA 2022.2 and 2022.4
 - home/end/pgUp/pgDown to jump to start/end of row/column
 - control+left/right/up/downArrow to jump to start/end of row/column (alternative shortcut key for the same result)
 - NVDA+left/up to read the whole row/column starting from the first cell without moving the current position of the cursor
 - NVDA+right/down for sayAll in row/column, i.e. read the cells of the current row/column, starting from the current cell and moving the cursor's position while reading until the last cell of the row/column.
* Remape some keys to avoid conflicts:
 - NVDA+upArrow/leftArrow becomes windows+upArrow/leftArrow (to read full column/row)
 - NVDA+downArrow/rightArrow becomes windows+downArrow/rightArrow (say all in column/row)
* Compatibility with NVDA 2023.1


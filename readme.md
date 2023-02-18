# Easy Table Navigator

*   Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 and beyond

This plugin adds a layer command to use simplified key combination to navigate table cells.
When the layered commands are enabled, you can perform the following actions:
- Navigate to the previous or next cell horizontally or vertically using arrow keys
- Navigate to the first or last cell of the row or the column using control+arrow keys or Home, End, PageUp and PageDown
- Read the whole row or column without moving the system caret using windows+leftArrow / windows+upArrow
- Read the row or column starting from the current cell using windows+rightArrow / windows+downArrow

Currently supported tables are:

* Browse mode (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Commands

* Toggles table navigator layer on and off (unassigned).

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

## Changes for 2.3

* It is now possible to disable table navigation layer from everywhere
* Compatibility with NVDA 2022.1
* Fix error when reloading the addon

## Changes for 2.2.1

* Fixed an error in some type of documents including Word and Outlook

## Changes for 2.2

* Update documentation style from addons template
* First translated version

## Changes for 2.1.1

* New author in manifest and documentation

## Changes for 2.1

* Compatibility with NVDA 2021.1

## Changes for 2.0

* Requires NVDA 2019.3 or later.
* Made various add-on messages translatable.

## Changes for 1.2

* Internal changes to support future NVDA releases.

## Changes for 1.1

* Fixed an issue where errors might be heard when spell checking a message in Outlook.

## Changes for 1.0

*   Initial release.

[1]: http://addons.nvda-project.org/files/get.php?file=etn

[2]: http://addons.nvda-project.org/files/get.php?file=etn-dev

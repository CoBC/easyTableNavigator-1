# Lakša navigacija kroz tabele  #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Preuzmi [stabilnu verziju ][1]
* Preuzmi [verziju u razvoju ][2]
* NVDA compatibility: 2019.3 and beyond

This plugin adds a layer command to use simplified key combination to
navigate table cells.  When the layered commands are enabled, you can
perform the following actions:

* Navigate to the previous or next cell horizontally or vertically using
  arrow keys
* Navigate to the first or last cell of the row or the column using
  control+arrow keys or Home, End, PageUp and PageDown
* Read the whole row or column without moving the system caret using
  windows+leftArrow / windows+upArrow
* Read the row or column starting from the current cell using
  windows+rightArrow / windows+downArrow

Trenutno podržane tabele su:

* Režim pretraživanja(Internet Explorer, Firefox, I tako dalje.).
* Microsoft Word.

## Komande

* Uključuje ili isključuje navigator tabela(Nedodeljeno).

## Changes for 2.4

For this release, many thanks goes to Cyrille Bougot for his work.

* Table navigation fixed in MS Word
* Introduce new commands following changes in NVDA 2022.2 and 2022.4

    * home/end/pgUp/pgDown to jump to start/end of row/column
    * control+left/right/up/downArrow to jump to start/end of row/column
      (alternative shortcut key for the same result)
    * NVDA+left/up to read the whole row/column starting from the first cell
      without moving the current position of the cursor
    * NVDA+right/down for sayAll in row/column, i.e. read the cells of the
      current row/column, starting from the current cell and moving the
      cursor's position while reading until the last cell of the row/column.

* Remaped some keys to avoid conflicts:

    * NVDA+upArrow/leftArrow becomes windows+upArrow/leftArrow (to read full
      column/row)
    * NVDA+downArrow/rightArrow becomes windows+downArrow/rightArrow (say
      all in column/row)

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

## Promene u 2.1.1

* Novi autor u manifestu i dokumentaciji

## Promene u 2.1

* Kompatibilnost uz NVDA 2021.1

## Promene u 2.0

* Zahteva NVDA 2019.3 ili noviji.
* Razne poruke dodatka se sada mogu prevesti.

## Promene u 1.2

* Interne promene za podršku budućih NVDA verzija.

## Promene u 1.1

* Popravljen problem gde može doći do grešaka prilikom provere pravopisa u
  outlooku.

## Promene u 1.0

*   Prva verzija.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

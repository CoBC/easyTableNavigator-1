# Jednostavno kretanje po tablici (Easy Table Navigator) #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2019.3 i novije verzije

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

Trenutačno podržane tablice su:

* Modus čitanja (Internet Explorer, Firefox, itd.).
* Microsoft Word.

## Naredbe

* Uključuje i isključuje kretanje po tablici (nedodijeljeno).

## Promjene u verziji 2.4

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

* Kompatibilnost s NVDA verzijom 2023.1.

## Promjene u verziji 2.3

* It is now possible to disable table navigation layer from everywhere
* Kompatibilnost s NVDA 2022.1
* Fix error when reloading the addon

## Izmjene u verziji 2.2.1

* Ispravljena je greška u nekim vrstama dokumenata uključujući Word i
  Outlook

## Izmjene u verziji 2.2

* Aktualiziran je stil dokumentacije iz predloška dodataka
* Prva prevedena verzija

## Izmjene u verziji 2.1.1

* Novi autor u manifestu i dokumentaciji

## Izmjene u verziji 2.1

* Kompatibilnost s NVDA 2021.1

## Izmjene u verziji 2.0

* Zahtijeva NVDA 2017.3 i noviji.
* Razne poruke ovog dodatka su sada prevodive.

## Izmjene u verziji 1.2

* Unutarnje promjene, kako bi se podržala buduća NVDA izdanja.

## Izmjene u verziji 1.1

* Ispravljena je greška koja je prouzrokovala reprodukciju zvuka pogreške
  prilikom provjere pravopisa u Outlooku.

## Izmjene u verziji 1.0

*   Prva verzija.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

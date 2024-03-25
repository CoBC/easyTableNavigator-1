# Easy Table Navigator #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Pobierz [Wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
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

Aktualnie obsługiwane tabele to:

* Tryb czytania (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Komendy

* Włącza i wyłącza nawigatora tabel (nieprzypisane).

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

## Zmiany w wersji 2.2.1

* Naprawiono błąd w niektórych typach dokumentów, w tym w programach Word i
  Outlook

## Zmiany w wersji 2.2

* Aktualizowanie stylu dokumentacji z szablonu dodatków
* Pierwsza przetłumaczona wersja

## Zmiany w wersji 2.1.1

* Nowy autor w manifeście i dokumentacji

## Zmiany w wersji 2.1

* Kompatybilność z NVDA 2021.1

## Zmiany dla wersji 2.0

* Wymaga wersji NVDA 2019.3 i nowsze.
* Od teraz różne komunikaty dodatku są przetłumaczone.

## Zmiany dla wersji 1.2

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Zmiany dla wersji 1.1

* Naprawiono problem dźwięków błędu które mogły się pojawiać podczas
  sprawdzania pisowni wiadomości w Outlook.

## Zmiany dla wersji 1.0

*   Pierwsze wydanie.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

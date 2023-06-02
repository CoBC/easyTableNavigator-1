# Nem Tabelnavigation #

* Forfattere: Corentin Bacqué-Cazenave, Joseph Lee
* Download [stabil version][1]
* Download [udviklingsversion][2]
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

I øjeblikket er følgende tabeller understøttet:

* Gennemsynstilstand (Internet Explorer, Firefox, osv.).
* Microsoft Word.

## Kommandoer

* Slå kommandolaget til tabelnavigering til/fra (ikke tilknyttet).

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

## Ændringer for 2.2.1

* Rettet en fejl for nogle typer af dokumenter, herunder Word og Outlook

## Ændringer for 2.2

* Opdater dokumentationsstilen fra tilføjelsesskabelon
* Første oversatte version

## Ændringer for 2.1.1

* Ny forfatter i manifest og dokumentation

## Ændringer i 2.1

* Kompatibilitet med NVDA 2021.1

## Ændringer i 2.0

* Kræver NVDA 2019.3 eller nyere.
* Oprettet forskellige tilføjelsesmeddelelser, der kan oversættes.

## Ændringer i 1.2

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Ændringer i 1.1

* Løste et problem, hvor man kunne høre fejl under stavekontrol af en
  meddelelse i Outlook.

## Ændringer i 1.0

*   Første udgivelse

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

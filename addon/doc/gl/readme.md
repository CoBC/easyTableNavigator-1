# Easy Table Navigator #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
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

As táboas actualmente soportadas son:

* Modo Exploración (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Ordes

* Activa ou desactiva a capa de navegador de táboa (sen asignar).

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

## Cambios para 2.2.1

* Arranxado un erro nalgúns tipos de documentos incluídos Word e Outlook

## Cambios para 2.2

* Actualizado estilo de documentación a partir do patrón de complementos
* Primeira versión traducida

## Cambios para 2.1.1

* Novo autor no manifesto e a documentación

## Cambios para 2.1

* Compatibilidade con NVDA 2021.1

## Cambios para 2.0

* Require NVDA 2019.3 ou posterior.
* Feitos traducibles varias mensaxes do complemento.

## Cambios para 1.2

* Cambios internos para soportar versións futuras de NVDA.

## Cambios para 1.1

* Correxido un fallo onde se poderían escoitar erros ó correxir a ortografía
  dunha mensaxe en Outlook.

## Cambios para 1.0

*   Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

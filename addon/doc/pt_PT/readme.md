# Navegador fácil em Tabelas #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Baixar [Versão estável][1]
* Baixar [Versão de desenvolvimento][2]
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

As tabelas actualmente suportadas são:

* Modo de navegação (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Comandos

* Alternar a activação ou desactivação do extra (não atribuída).

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

## Alterações para 2.2.1

* Corrigido um erro em alguns tipos de documentos, incluindo Word e Outlook

## Mudanças para 2.2

* Actualização do estilo de documentação a partir do modelo de addons
* Primeira versão traduzida

## Alterações para 2.1.1

* Novo autor em manifesto e documentação

## Mudanças para 2.1

* Compatibilidade com NVDA 2021.1

## Alterações para a versão 2.0

* Requer o NVDA 2019.3 ou posterior.
* Tornou várias mensagens do extra traduzíveis.

## Mudanças para a versão 1.2

* Alterações internas para apoiar futuros lançamentos do NVDA.

## Alterações para 1.1

* Corrigido um problema em que se ouviam erros aquando da verificação
  ortográfica de uma mensagem no Outlook.

## Alterações para 1.0

*   Lançamento inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

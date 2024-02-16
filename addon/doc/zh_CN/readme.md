# Easy Table Navigator-简易表格导航器 #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* 下载 [稳定版][1]
* 下载 [开发板][2]
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

目前支持的表格有：

* 浏览模式（Internet Explorer、 Firefox等）。
* Microsoft Word 文档。

## 快捷键

* 开关简易导航模式（未分配），开启后，您可以使用四个光标键进行表格导航。

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

## 版本 2.2.1

* 修复了某些类型的文档（包括 Word 和 Outlook）中的错误

## 版本 2.2

* 使用插件模板更新文档样式
* 首个可翻译版本

## 版本 2.1.1

* 更新 manifest 文件和文档中的作者信息

## 版本 2.1

* 兼容 NVDA 2021.1

## 版本2.0

* 需要NVDA 2019.3或更高版本。
* 使插件的各种语言条目可翻译。

## 版本1.2

* 内部更改，为支持新版 NVDA 做准备。

## 版本1.1

* 修复了在Outlook中拼写检查邮件时可能会抛出错误的问题。

## 版本1.0

*   发布初始版本。

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

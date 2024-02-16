# Einfacher Tabellen-Navigator #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.3 und neuer

Diese NVDA-Erweiterung fügt ein Navigationsbefehl hinzu, um vereinfachte
Tastenkombinationen zur Navigation in Tabellenzellen zu verwenden. Wenn die
Navigationsbefehle aktiviert sind, können Sie die folgenden Aktionen
durchführen:

* Mit den Pfeiltasten horizontal oder vertikal zur vorherigen oder nächsten
  Zelle navigieren
* Zur ersten oder letzten Zelle der Zeile oder Spalte springen mit den
  Tasten Strg+Pfeiltaste oder Pos1, Ende, Seite nach oben/unten
* Die ganze Zeile oder Spalte vorlesen, ohne den System-Cursor mit
  Windows+Pfeiltaste nach oben/links mitzuziehen
* Die Spalte oder Zeile ab der aktuellen Zelle vorlesen mit
  Windows+Pfeiltaste nach unten/rechts

Derzeit unterstützte Tabellen sind:

* Lesemodus (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Befehle

* Schaltet die Tabellennavigation ein und aus (nicht zugeordnet).

## Änderungen in 2.4

Für diese Veröffentlichung geht ein großer Dank an Cyrille Bougot für die
Arbeit.

* Tabellen-Navigation in Microsoft Word behoben
* Einführung neuer Befehle auf Grund der Änderungen in NVDA 2022.2 und
  2022.4

    * Pos1/Ende/Seite nach oben/unten, um zum Anfang bzw. Ende einer Spalte
      bzw. Zeile zu springen
    * Strg+Pfeiltaste nach oben/unten/links/rechts, um zum Anfang bzw. Ende
      einer Spalte bzw. Zeile zu springen (alternative Tastenkombination für
      dasselbe Ergebnis)
    * NVDA+Pfeiltaste nach oben/links, um die gesamte Spalte bzw. Zeile ab
      der ersten Zelle vorzulesen, ohne die aktuelle Position des Cursors zu
      verschieben
    * NVDA+Pfeiltaste nach unten/rechts für Alles Vorlesen in der Spalte
      bzw. Zeile, d. h., die Zellen der aktuellen Spalte bzw. Zeile
      vorzulesen, beginnend mit der aktuellen Zelle und die Position des
      Cursors während des Vorlesens bis zur letzten Zelle der Spalte
      bzw. Zeile verschieben.

* Einige Tasten wurden geändert, um Konflikte zu vermeiden:

    * NVDA+Pfeiltaste nach oben/links wird zu Windows+Pfeiltaste nach
      oben/links (gesamte Spalte bzw. Zeile vorlesen)
    * NVDA+Pfeiltaste nach unten/rechts wird zu Windows+Pfeiltaste nach
      unten/rechts (z. B. alle in Spalte bzw. Zeile)

* Kompatibel mit NVDA 2023.1

## Änderungen in 2.3

* Es ist nun möglich, die Tabellen-Navigationsebene von überall aus zu
  deaktivieren
* Kompatibel mit NVDA 2022.1
* Fehler beim Neuladen der NVDA-Erweiterung behoben

## Änderungen in 2.2.1

* Ein Fehler in einigen Word- und Outlook-Dokumenten wurde behoben

## Änderungen in 2.2

* Aussehen der Dokumentation über die Erweiterungsvorlage aktualisiert
* Erste übersetzte Version

## Änderungen in 2.1.1

* Neuer Autor in Manifest und Dokumentation

## Änderungen in 2.1

* Kompatibilität mit NVDA 2021.1

## Änderungen in 2.0

* Benötigt NVDA 2019.3 oder neuer.
* Verschiedene Meldungen der Erweiterung übersetzbar gemacht.

## Änderungen in 1.2

* Interne Änderungen zur Unterstützung zukünftiger NVDA-Versionen.

## Änderungen in 1.1

* Ein Problem wurde behoben, wonach Fehlertöne während der
  Rechtschreibprüfung in Outlook zu hören waren.

## Änderungen in 1.0

*   Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

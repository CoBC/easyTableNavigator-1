# Helppo taulukossa liikkuminen #

* Tekijät: Corentin Bacqué-Cazenave ja Joseph Lee
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2019.3 ja sitä uudemmat

Tämä lisäosa lisää NVDA:han komentokerroksen, jonka avulla voi käyttää
yksinkertaistettua näppäinyhdistelmää taulukon solujen välillä
liikkumiseen. Voit suoritta seuraavia toimintoja, kun komentokerroskomennot
ovat käytössä:

* Siirrä edelliseen tai seuraavaan soluun vaaka- tai pystysuunnassa
  nuolinäppäimiä käyttäen
* Siirrä rivin tai sarakkeen ensimmäiseen tai viimeiseen soluun
  Ctrl+nuolinäppäimiä tai Home-, End-, Page up- ja Page down -näppäimiä
  käyttäen
* Lue koko rivi tai sarake siirtämättä järjestelmäkohdistinta
  näppäinyhdistelmillä Win+Nuoli vasemmalle / Win+Nuoli ylös
* Lue rivi tai sarake nykyisestä solusta alkaen näppäinyhdistelmillä
  Win+Nuoli oikealle / Win+Nuoli alas

Taulukoita tuetaan tällä hetkellä:

* Selaustilassa (Internet Explorer, Firefox jne)
* Microsoft Wordissa

## Komennot

* Ottaa käyttöön tai poistaa käytöstä komentokerroksen (ei määritetty)

## Muutokset versiossa 2.4

Tästä julkaisusta saamme kiittää Cyrille Bougot'ta.

* Taulukkonavigointi korjattu MS Wordissa
* Lisätty uusia komentoja NVDA 2022.2:ssa ja 2022.4:ssä tehtyjen muutosten
  mukaisesti

    * Home/End/Page up/Page down rivin tai sarakkeen alkuun tai loppuun
      siirtämiseen
    * Ctrl+Nuoli vasemmalle/oikealle/ylös/alas rivin tai sarakkeen alkuun
      tai loppuun siirtämiseen (vaihtoehtoinen näppäinkomento samalle
      toiminnolle)
    * NVDA+Nuoli vasemmalle/ylös koko rivin tai sarakkeen lukemiseen
      ensimmäisestä solusta alkaen siirtämättä kohdistinta
    * NVDA+Nuoli oikealle/alas rivin tai sarakkeen jatkuva luku, ts. lukee
      nykyisen rivin tai sarakkeen solut nykyisestä solusta lähtien
      viimeiseen saakka ja siirtää samalla kohdistinta.

* Osa näppäinkomennoista uudelleenmääritelty ristiriitojen välttämiseksi:

    * NVDA+Nuoli ylös/vasemmalle on nyt Win+Nuoli ylös/vasemmalle (lukee
      koko sarakkeen tai rivin)
    * NVDA+Nuoli alas/oikealle on nyt Win+Nuoli alas/oikealle (sarakkeen tai
      rivin jatkuva luku)

* Yhteensopivuus NVDA 2023.1:lle

## Muutokset versiossa 2.3

* Taulukkonavigointikerroksen käytöstä poistaminen on nyt mahdollista mistä
  tahansa
* Yhteensopivuus NVDA 2022.1:lle
* Korjattu virhe, joka ilmeni lisäosaa uudelleenladattaessa

## Muutokset versiossa 2.2.1

* Korjattu virhe  määrätyn tyyppisissä asiakirjoissa, Word ja Outlook mukaan
  lukien

## Muutokset versiossa 2.2

* Dokumentaation tyyli päivitetty lisäosamallista
* Ensimmäinen käännetty versio

## Muutokset versiossa 2.1.1

* Uusi tekijä manifestissa ja dokumentaatiossa

## Muutokset versiossa 2.1

* Yhteensopivuus NVDA 2021.1:n kanssa

## Muutokset versiossa 2.0

* Vaatii NVDA 2019.3:n tai uudemman.
* Useat lisäosan viestit ovat nyt käännettävissä eri kielille.

## Muutokset versiossa 1.2

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Muutokset versiossa 1.1

* Korjattu ongelma, joka aiheutti sen, että Outlookissa saattoi kuulua
  virheitä viestiä oikoluettaessa.

## Muutokset versiossa 1.0

*   Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

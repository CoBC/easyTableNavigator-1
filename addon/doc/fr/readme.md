# Easy Table Navigator #

* Auteurs : Corentin Bacqué-Cazenave, Joseph Lee
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* Compatibilité NVDA : 2019.3 et au-delà

Cette extension ajoute une commande séquentielle pour utiliser une
combinaison de touches simplifiée pour naviguer dans les cellules du
tableau. Lorsque les commandes séquentielles sont activées, vous pouvez
effectuer les actions suivantes :

* Accédez à la cellule précédente ou suivante horizontalement ou
  verticalement à l'aide des touches fléchées
* Accédez à la première ou à la dernière cellule de la ligne ou de la
  colonne à l'aide des touches contrôle+touches fléchées ou début, fin, page
  précédente et page suivante
* Lire la ligne ou la colonne entière sans déplacer le curseur système à
  l'aide de Windows+flèche gauche / Windows+flèche haut
* Lire la ligne ou la colonne depuis la cellule courante à l'aide de
  Windows+flèche droite / Windows+flèche bas

Les tableaux actuellement supportés son :

* Mode navigation (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Commandes

* Active ou désactive les commandes séquentielles de navigation dans les
  tableaux (non assignés).

## Changements pour la version 2.4

Pour cette version, merci à Cyrille Bougot pour son travail.

* Navigation de tableau corrigée dans MS Word
* De nouvelles commandes de navigation pour les tableaux ont été introduites
  suivant les modifications de NVDA 2022.2 et 2022.4

    * Début / fin / page précédente / page suivante pour aller au début /
      fin de la ligne / colonne
    * Contrôle+gauche / droite / flèches haut / bas pour aller au début /
      fin de la ligne  / colonne (touche de raccourci alternative pour le
      même résultat)
    * NVDA+gauche / haut pour lire la ligne / colonne entière depuis la
      première cellule sans déplacer la position actuelle du curseur
    * NVDA+droite / bas pour dire tout dans la ligne / colonne, c'est-à-dire
      lire les cellules de la ligne / colonne courante, depuis la cellule
      courante et en déplaçant la position du curseur tout en lisant jusqu'à
      la dernière cellule de la ligne / colonne.

* Remappé certaines touches pour éviter les conflits :

    * NVDA+flèche haut / flèche gauche devient Windows+flèche haut / flèche
      gauche ( pour lire la colonne / ligne entière)
    * NVDA+flèche bas / flèche droite devient Windows+flèche bas / flèche
      droite (dire tout dans la colonne / ligne)

* Compatibilité avec NVDA 2023.1

## Changements pour la version 2.3

* Il est désormais possible de désactiver les commandes séquentielles de
  navigation dans les tableaux de partout
* Compatibilité avec NVDA 2022.1
* Correction de l'erreur lors du rechargement de l'extension

## Changements pour la version 2.2.1

* Correction d'une erreur dans certains types de documents incluant Word et
  Outlook

## Changements pour la version 2.2

* Mise à jour du style de la documentation à partir du modèle d'extensions
* Première version traduite

## Changements pour la version 2.1.1

* Nouvel auteur dans le manifest et la documentation

## Changements pour la version 2.1

* Compatibilité avec NVDA 2021.1

## Changements pour la version 2.0

* Nécessite NVDA 2019.3 ou ultérieure.
* Plusieurs messages sont rendus traduisibles.

## Changements pour la version 1.2

* Modifications internes pour prendre en charge les futures versions de
  NVDA.

## Changements pour la version 1.1

* Correction d'un problème où les erreurs pourraient être entendus lors
  d'une vérification orthographique d'un message  dans Outlook.

## Changements pour la version 1.0

*   Première version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

# Улеснена навигация в таблиците (Easy Table Navigator) #

* Authors: Corentin Bacqué-Cazenave, Joseph Lee
* Изтегляне на [стабилна версия][1]
* Изтегляне на [тестова версия][2]
* Съвместимост с NVDA: от 2019.3 и по-нови версии

Тази добавка добавя слоеви команди за използване на опростени клавишни
команди за навигиране в клетките на таблица. Когато слоевите команди са
задействани, можете да извършвате следните действия:

* Придвижване до предишната или следващата клетка хоризонтално или
  вертикално с помощта на клавишите със стрелките
* Придвижване до първата или последната клетка на реда или колоната, чрез
  използване на клавишните команди Control+Клавишите със стрелките или Home,
  End, Page Up и Page Down
* Прочитане на целия ред или колона, без преместване на системната каретка,
  чрез използване на Windows+Стрелка наляво / Windows+Стрелка нагоре
* Прочитане на реда или колоната, започвайки от текущата клетка, чрез
  използване на Windows+Стрелка надясно / Windows+Стрелка надолу

Текущо поддържаните таблици са:

* В режим на преглед (Internet Explorer, Firefox и т.н.).
* В Microsoft Word.

## Команди

* Включва/изключва слоя за команди за навигация в таблиците (неприсвоена).

## Промени във версия 2.4

За това издание отправяме огромни благодарности към Cyrille Bougot за труда
му.

* Поправена е навигацията в таблици в MS Word
* Въведени са нови команди след промените в NVDA 2022.2 и 2022.4

    * Home/End/Page Up/Page Down за преминаване към началото/края на
      ред/колона
    * Control+Стрелка наляво/надясно/нагоре/надолу за преминаване към
      началото/края на ред/колона (алтернативна команда за бърз достъп за
      същия резултат)
    * NVDA+Стрелка наляво/нагоре за четене на целия ред/колона, започвайки
      от първата клетка, без преместване на курсора от текущата му позиция
    * NVDA+Стрелка надясно/надолу за прочитане на всичко в реда/колоната
      (т.е. прочитане на клетките на текущия ред/колона, започвайки от
      текущата клетка и премествайки позицията на курсора по време на
      четенето, до последната клетка на реда/колоната.

* Преназначени са някои клавишни команди, за да се избегнат конфликти:

    * NVDA+Стрелка нагоре/Стрелка наляво става Windows+Стрелка
      нагоре/Стрелка наляво (за четене на всичко в колоната/реда)
    * NVDA+Стрелка надолу/Стрелка надясно става Windows+Стрелка
      надолу/Стрелка надясно (прочитане на всичко в колонтаа/реда)

* Съвместимост с NVDA 2023.1

## Промени във версия 2.3

* Вече е възможно от всякъде да се изключи слоя за навигация в таблици
* Съвместимост с NVDA 2022.1
* Поправена е грешка при презареждане на добавката

## Промени във версия 2.2.1

* Поправена е грешка в някои видове документи, включително такива на Word и
  Outlook

## Промени във версия 2.2

* Актуализиран е стила на документацията от шаблона за добавки
* Първа преведена версия

## Промени във версия 2.1.1

* Нов автор в manifest файла и документацията

## Промени във версия 2.1

* Съвместимост с NVDA 2021.1

## Промени във версия 2.0

* Изисква се NVDA 2019.3 или по-нова версия.
* Разни съобщения на тази добавка вече могат да се превеждат.

## Промени във версия 1.2

* Вътрешни промени с цел поддържане на бъдещи издания на NVDA.

## Промени във версия 1.1

* Поправен е проблем, при който може да бъдат изведени звукови сигнали за
  грешки при извършване на правописна проверка на съобщение в Outlook.

## Промени във версия 1.0

*   Първоначално издание.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

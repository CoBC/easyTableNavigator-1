# Easy Table Navigator #

* Autores: Corentin Bacqué-Cazenave, Joseph Lee
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2019.3 en adelante

Este complemento añade una capa de órdenes para usar combinaciones de
teclado simplificadas para navegar por celdas de tablas. Cuando las órdenes
de capa están activadas, puedes realizar las siguientes acciones:

* Navegar a la siguiente celda o la anterior horizontal o verticalmente
  usando las flechas
* Navegar a la primera o última celda de la fila o columna usando
  control+flechas o inicio, fin, retroceso de página y avance página
* Leer la fila o columna enteras sin mover el cursor del sistema usando
  windows+flecha izquierda o windows+flecha arriba
* Leer la fila o columna empezando en la celda actual usando windows+flecha
  derecha o windows+flecha abajo

Las tablas actualmente soportadas son:

* Modo Exploración (Internet Explorer, Firefox, etc.).
* Microsoft Word.

## Órdenes

* Activa o desactiva la capa de navegador de tabla (sin asignar).

## Cambios para 2.4

En esta versión, muchos agradecimientos van hacia Cyrille Bougot por su
trabajo.

* Corregida la navegación por tablas en Microsoft Word
* Se introducen nuevas órdenes siguiendo los cambios en NVDA 2022.2 y 2022.4

    * inicio / fin / retroceso página / avance página para saltar al inicio
      o fin de la fila o columna
    * control+flechas izquierda, derecha, arriba y abajo para saltar al
      inicio o fin de la fila o columna (teclas de atajo alternativas para
      el mismo resultado)
    * NVDA+flechas izquierda o arriba para leer la fila o columna enteras
      desde la primera celda sin mover la posición actual del cursor
    * NVDA+flechas derecha o abajo para verbalizar todo en la fila o
      columna, es decir, leer las celdas de la fila o columna actual,
      empezando en la celda actual y moviendo la posición del cursor
      mientras se lee hasta la última celda de la fila o columna.

* Se han reasignado algunas teclas para evitar conflictos:

    * NVDA+flechas arriba / izquierda se convierte en windows+flechas arriba
      / izquierda (para leer la columna o fila completas)
    * NVDA+flechas abajo / derecha se convierte en windows+flechas abajo /
      derecha (verbalizar todo en columna o fila)

* Compatibilidad con NVDA 2023.1

## Cambios para 2.3

* Ahora es posible desactivar la capa de navegación por tablas desde
  cualquier parte
* Compatibilidad con NVDA 2022.1
* Corregido un problema al recargar el complemento

## Cambios para 2.2.1

* Corregido un error en algunos tipos de documentos, incluyendo Word y
  Outlook

## Cambios para 2.2

* Actualizado el estilo de la documentación desde la plantilla de
  complementos
* Primera versión traducida

## Cambios para 2.1.1

* Nuevo autor en el manifiesto y la documentación

## Cambios para 2.1

* Compatibilidad con NVDA 2021.1

## Cambios para 2.0

* Se requiere NVDA 2019.3 o posterior.
* Se han hecho traducibles diversos mensajes del complemento.

## Cambios para 1.2

* Cambios internos para dar soporte a versiones futuras de NVDA.

## Cambios para 1.1

* Corregido un fallo donde podrían escucharse errores al corregir la
  ortografía de un mensaje en Outlook.

## Cambios para 1.0

*   Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev

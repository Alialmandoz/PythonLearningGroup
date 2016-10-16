# Encontrar texto
La idea del proyecto es filtrar repetidos en un archivo de texto y mantenerlo en alguna estuctura de datos para usarlos posteriormente

## Composicion de datos
El archivo tene entradas de datos distribuidos de la siguiente manera (los tabs no los lee el interprete)
- Un espacio inicial
- Valor numérico de 7 caracteres
- Un espacio
- Fecha formato dd/mm/aa (algunos no lo tienen)
- Tres espacios (algunos no lo tienen)
- 33 caracteres dedicados a apellido y nombre (algunos lo tienen)
- Valor alfanumérico de longitud 5 (algunos no lo tienen)
- Un espacio variable, ente 1 y 5 espacios
- Un valor de punto flotante
- Un espacio
- Uno o dos datos

El archivo tambien tiene renglones con informes, no se analizan

## Modo de uso
### simple.py
Simplemente correr `python3 simple.py` en la consola
### main.py
Correr en la consola `python3 main.py [nombre de archivo aquí]` en la consola

## Explicación de los scripts
El archivo main contiene 3 funciones para modularizar sus funcionalidades, una recibe un string (el renglón), lo analiza y depura los datos que son necesarios, si encuentra inconsistencias, escapa de la función y no sigue analizando el resto del renglón.
Una segunda función, recibe el nombre del archivo, y una funciones, y solo recorre el archivo que se le pasa, aplica la función al renglón. Luego retorna lo obtenido

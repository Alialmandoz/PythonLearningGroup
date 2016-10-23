# Actividad: Encontrar texto
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

Correr en la consola python main.py `[nombre de archivo aquí]` en la consola    
Da como resultado un archivo output.txt

## Explicacion
El programa estaria conformado por distintas clases:    
**Resultado** - Objeto conformado por las distintas partes de la 
la lista procesada de DataStructure.    
**DataStructure** - Objeto que surge de aqui luego de procesar el archivo
 de texto es una lista de lista con todos los valores utiles 
 para ser procesados.    
**Output** - Objeto que mantiene en si mismo todos los valores ademas
de poseer la funcion de generar el archivo output.txt.    
Main se encarga de llamar a output con el parametro ingresado por consola

## tests
Hay una serie de pruebas unitarias hechas sobre Resultado y DataStructure 
las cuales se ejecutan corriendo pytest en la carpeta test.

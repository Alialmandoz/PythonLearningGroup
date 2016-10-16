import sys
from pprint import pprint

def procesar_renglon(cadena):
    """Esta funcion toma una cadena de texto y procesa los datos y los devuelve
    en alguna estructura"""
    if '/' not in cadena:
        return
    primero_numero = cadena[1:8]
    fecha = cadena[10:18]
    apellido_nombre = cadena[20:54]

    apellido_nombre = apellido_nombre.split()
    if len(apellido_nombre) == 0:
        return

    codigo = cadena[56:61]
    final = cadena[63:]
    apellido = apellido_nombre[0]
    del apellido_nombre[0]

    nombre = ""
    for i in apellido_nombre:
        nombre += " " + i
    else:
        nombre = nombre[1:]

    try:
        primero_numero = int(primero_numero)
    except ValueError:
        print("El primer valor debe ser un número, revisar fuente")
    return {'numero': primero_numero, 'apellido': apellido, 'nombre': nombre, 'codigo': codigo, 'fecha': fecha }

def procesar_datos(elem):
    """Esta funcion maneja los datos obtenidos, procesados por la funcion argumento"""
    aux = elem['numero']
    del elem['numero']
    #print(elem)conjunto[ aux ] = elem
    conjunto[ aux ] = elem

def recorrer_archivo(archivo, func1, func2):
    """Esta funcion recorre el archivo de texto que se le pasa y a cada renglon
    le aplica la funcion de argumento"""
    conjunto = {}

    with open( archivo, 'r' ) as file:
        todos = file.readlines()
        for renglon in todos:
            aux = func1(renglon)
            if aux:
                func2(aux)
        else:
            return conjunto

nombre_del_archivo = sys.argv[1] #argumentos pasados por consola [0] es el script, [1] el archivo de texto

resultado = recorrer_archivo( nombre_del_archivo, procesar_renglon, procesar_datos )
print("Tu resultado tiene {0} lineas".format( len(resultado) ) )
pprint(resultado)
print("Once again. Tu resultado tiene {0} lineas".format( len(resultado) ) )

import sys
from output import Output


if __name__=='__main__':
	nombre_del_archivo = sys.argv[1] #argumentos pasados por consola [0] es el script, [1] el archivo de texto
	o = Output(nombre_del_archivo)
	o.create_output()

import csv
import json
import os

os.system("cls")
archivo_a_leer="listado.txt"
with open(archivo_a_leer,"r") as archivo:
    contenido=archivo.read()
    print(contenido)
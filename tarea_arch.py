import csv
import json
import os

x=0
os.system("cls")
archivo_a_leer="listado.txt"
with open(archivo_a_leer,"r") as archivo:
    contenido=archivo.read()
    contenido=contenido.split("\n")

    while x<len(contenido):
        escritura=contenido[x].split(",")
        with open("listado.csv","a",newline="") as excel:
            escritor_csv = csv.writer(excel)
            escritor_csv.writerow(escritura)

        x=x+1
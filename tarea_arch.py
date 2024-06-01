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

with open("listado.csv","r",newline="") as excel:
    lector_cvs=csv.reader(excel)
    for x in lector_cvs:
        num=int(x[2])
        if num>200000000:
            empresa={"rut":x[0],
                     "nombre":x[1],
                     "ventas":x[2],
                     "contribuyente":"Gran Contribuyente"}
        elif num<=200000000 and num>100000000 :
            empresa={"rut":x[0],
                     "nombre":x[1],
                     "ventas":x[2],
                     "contribuyente":"Mediano Contribuyente"}
        else:
            empresa={"rut":x[0],
                     "nombre":x[1],
                     "ventas":x[2],
                     "contribuyente":"Pequeno Contribuyente"}
        with open("Listado.json","+a") as diccionario:
            json.dump(empresa,diccionario)
            diccionario.write("\n")
            
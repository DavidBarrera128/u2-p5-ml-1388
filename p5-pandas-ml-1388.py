import numpy as np
import pandas as pd
## David Barrera NC = 1388
## datos matriz
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
## poner nombre de las columnas
## y almacenar la tabla en la variable df dataframe
print("--- Datos a partir de una matriz 4 x 3 ---")
df = pd.DataFrame(datos_alumno,columns=["ci","marcas","paquete"])
print(df)
## datos a partir de un diccionario
print("--- Datos a partir de un diccionario ---")
alumno_dicionario ={
    "nombre":["Eliseo","Joel","Pedro","Nicole","Dilan","Jesse"],
    "califa":[60,90,100,80,70,80],
    "edad":[64,15,16,16,18,14]
}

estudiante = pd.DataFrame(alumno_dicionario)
print(estudiante)
print("David Barrera NC = 1388")
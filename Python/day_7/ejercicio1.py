#Pandas es una librería para manipular y analizar datos estructurados. 
#En vez de abrir y leer un archivo manualmente lo podemos hacer mediante pandas, importemoslo
import pandas as pd

df = pd.read_csv("Python/day_4/paises.csv")
#De esta manera ya hemos cargados nuestros datos 
#APUNTE:  df es la abreviación de Data Frame que es una tabla de datos de dos dimensiones

print(df)

print()
print(df.head())
#Nos aparecen las primeras filas

print()
print(df.info())
#Nos muestra la información de la tabla

print()
print(df.describe())
#Nos muestra distintas características de los datos

print(df["Paro"])
#APUNTE: El Data Frame es la tabla completa, y una serie es cada una de las columnas

#Hagamos un filtro al igual que con los numpys
print("Probamos el filtrado")
filtrado = df["Inflacion"] < 2.5
print(df[filtrado])
#En este caso queremos crear una clasificación
#Para ello crearemos una nueva columna donde se clasificará un pais a partir de su paro
#Paro < 5 => "Bajo"
#Paro entre 5 y 8 => "Medio"
#Paro >= 8 => "Alto"
#Para ello usaremos pd.cut()

import pandas as pd

df = pd.read_csv("Python/day_4/paises.csv")

df["Situacion_paro"] = pd.cut(df["Paro"], [0,5,8, float("inf")], labels = ["Bajo", "Medio", "Alto"])
#El float("inf") significa infinito positivo, todo número mayor que ocho se tomará como un paro alto

print(df)
#De esta manera podemos convertir una variable numñerica en catergorias de intervalos, labels significa etiqueta

#Ahora usemos groupby(), una de las herramientas más importantes de Pandas
#La idea es agrupar por situacion de paro el dataframe y hacer un cálculo en cada uno de los grupos

print(df.groupby("Situacion_paro")["PIB"].mean())
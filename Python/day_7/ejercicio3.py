import pandas as pd

#En este caso añadiremos una nueva columna en nuestro data frame a partir de otras ya existentes
df = pd.read_csv("Python/day_4/paises.csv")

#Queremos calcular una columna llamada PIB_miles, dividido entre 1000
df["PIB_miles"] = df["PIB"]/1000

print(df)
import pandas as pd

#Leamos el archivo
df = pd.read_csv("Python/day_4/paises.csv")

#Mostremos los paises de nuestro csv
paises = df["Pais"]
print(paises)

#Mostremos los paises con un PIB mayor a 2000
filtrado = df["PIB"] > 2000
print(paises[filtrado])

#Mostremos los paises con un paro menor que 6

filtrado_paro = df["Paro"] < 6
print(paises[filtrado_paro])

#Ahora queremos mostrar solamente el nombre del país y su PIB para los países cuyo paro sea inferior al 6%.
paises_pib = df[["Pais", "PIB"]]
print(paises_pib)
print()

print(paises_pib[filtrado_paro])

#Ahora hagamos dos filtrados en la misma línea de código
#El ejercicico trata de mostrar los países cuyo PIB sea mayor a 2000 y paro menor a 6
filtrado_paro_pib = (df["PIB"] > 2000) & (df["Paro"] < 6)

print(df[filtrado_paro_pib])
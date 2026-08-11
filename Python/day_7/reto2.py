#Quremos saber cuantos países hay en cada categoría de paro
import pandas as pd

df = pd.read_csv("Python/day_4/paises.csv")

df["Situacion_paro"] = pd.cut(df["Paro"], [0,5,8, float("inf")], labels = ["Bajo", "Medio", "Alto"])

print(df)

df.groupby("Situacion_paro")["Pais"].count
#Ahora nos preguntamos ¿cual es la inflacion media de cada categoria de paro?

print(df.groupby("Situacion_paro")["Inflacion"].mean())

#Ahora mostraremos el PIB medio de los paises con inflacion media
#Primero filtramos para que solo me salga los paises con paro medio

filtrado = df["Situacion_paro"] == "Medio"
print(f"PIB medio de los paises con paro medio: {df[filtrado]["PIB"].mean()}")
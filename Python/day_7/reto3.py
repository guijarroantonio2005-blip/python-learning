#Hagamos finalmente el siguiente reto
import pandas as pd

df = pd.read_csv("Python/day_4/paises.csv")
#Queremos crear un resumen que nos muestre las siguientes caracteristicas
#Pais mayor PIB
#Pais con inflacion más baja
#Paro medio de todos los paises

#Esto vez usaremos iloc
df_ordenado_pib = df.sort_values("PIB", ascending = False)
print(df_ordenado_pib)

print(f"El pais con mayor PIB es {df_ordenado_pib.iloc[0]["Pais"]}")

df_ordenada_inflacion = df.sort_values("Inflacion")
print(f"El pais con menor inflacion es {df_ordenada_inflacion.iloc[0]["Pais"]}")

print(f"El paro medio de todos los paises es {df["Paro"].mean()}")
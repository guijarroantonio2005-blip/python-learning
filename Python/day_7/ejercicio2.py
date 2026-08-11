import pandas as pd

#ordenemos los datos para ellos usamos sort

df = pd.read_csv("Python/day_4/paises.csv")

print(df.sort_values("Pais"))

df.sort_values("Pais")

print()

print(df)
#NOTA: No es como java que la data frame te la cambia cuando usas el sort, cosa muy interesante que cambia
#Uno de los métodos memorizados de java, en python es diferente, entonces lo que haremos será nombrar a la lista
#ordenada

df_ordenada_paises = df.sort_values("Pais")
print(df_ordenada_paises)


#Ahora hagamoslo por PIB pero ordenado de mayor a menor
df_ordenada_PIB_mayor_a_menor = df.sort_values("PIB",  ascending = False) 
print(df_ordenada_PIB_mayor_a_menor)

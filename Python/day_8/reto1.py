import pandas as pd

datos = {
    "Pais": ["España", "Francia", "Alemania", "Italia"],
    "PIB": [1500, 2800, None, 2100],
    "Paro": [11.5, None, 3.2, 7.6]
}

df = pd.DataFrame(datos)

#Mostremos cuantos valores faltan en cada serie
print(df.isnull().sum())

#Creemos el data frame limpio
df_limpio = df.dropna()
print(df_limpio)
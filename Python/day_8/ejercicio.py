import pandas as pd

df = pd.read_csv("Python/day_4/paises.csv")
print(df)

print(df.isnull())
print(df.isnull().sum())

#Creemos el siguiente problema
datos = {
    "Pais": ["España", "Francia", "Alemania", "Italia"],
    "PIB": [1500, 2800, None, 2100],
    "Paro": [11.5, None, 3.2, 7.6]
}

df = pd.DataFrame(datos)

print(df)

#vamos a detectar esos valores nulos
print(df.isnull())
print(df.isnull().sum())

df_limpio = df.dropna()
print(df_limpio)
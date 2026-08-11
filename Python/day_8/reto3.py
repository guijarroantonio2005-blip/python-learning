import pandas as pd

datos = {
    "Pais": ["España", "Francia", "Alemania", "Italia", "Italia"],
    "PIB": [1500, 2800, 4200, 2100, 2100],
    "Paro": [11.5, 7.3, 3.2, 7.6, 7.6]
}

df = pd.DataFrame(datos)

print(df)
print(df.duplicated())

df_limpio = df.drop_duplicates()
print(df_limpio)
import pandas as pd

datos = {
    "Pais": ["España", "Francia", "Alemania", "Italia"],
    "PIB": [1500, 2800, None, 2100],
    "Paro": [11.5, None, 3.2, 7.6]
}

df = pd.DataFrame(datos)

#rellenamos los datos con la media de la serie correspondiente

media_PIB = df["PIB"].mean()
df["PIB"] = df["PIB"].fillna(media_PIB)
print(df)

media_Paro = df["Paro"].mean()
df["Paro"] = df["Paro"].fillna(media_Paro)
print(df)
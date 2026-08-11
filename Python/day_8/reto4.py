#Modifiquemos nuestra tabla
import pandas as pd

import pandas as pd

datos = {
    "Pais": ["España", "Francia", "Alemania", "Italia", "Italia"],
    "PIB": [1500, 2800, 4200, 2100, 2100],
    "Paro": [11.5, 7.3, 3.2, 7.6, 7.6]
}

df = pd.DataFrame(datos)

print(df)

#Cambiemos el nombre de las columnas
print()
df = df.rename(columns = {"Pais":"pais"})
df = df.rename(columns = {"PIB":"pib"})
df = df.rename(columns = {"Paro":"paro"})
print(df)

df.to_csv("paises_limpio.csv", index=False)
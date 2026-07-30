#Definamos funciones con diccionario



def mostrar_pais(pais):
    print(f"{pais["pais"]} tiene un PIB de {pais["PIB"]} y una inflación del {pais["inflacion"]}")

paises = [{"pais": "España", "PIB": 1500, "inflacion":2.8},{"pais": "Francia", "PIB": 2500, "inflacion":2.9}, {"pais": "Alemania", "PIB": 4600, "inflacion":2.87},{"pais": "Estados Unidos", "PIB": 6500, "inflacion":2.4}]

for pais in paises:
    mostrar_pais(pais)

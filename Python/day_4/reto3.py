#Encontramos el país con mayor PIB, menor inflación y mayor paro

#Abrimos el archivo

archivo = open("Python/day_4/paises.csv")

#Saltamos la primera linea

next(archivo)

pais_mayor_pib = ""
mayor_pib = 0

pais_menor_inflacion = ""
menor_inflacion = 10000

pais_mayor_paro = ""
mayor_paro = 0

for linea in archivo:

    datos = linea.strip().split(",")

    pais = datos[0]
    pib = float(datos[1])
    inflacion = float(datos[2])
    paro = float(datos[3])

    if mayor_pib < pib:
        mayor_pib = pib
        pais_mayor_pib = pais

    if inflacion < menor_inflacion:
        menor_inflacion = inflacion
        pais_menor_inflacion = pais

    if paro > mayor_paro:
        mayor_paro = paro
        pais_mayor_paro = pais


print(f"{pais_mayor_pib} es el pais con mayor PIB siendo este de {mayor_pib}\n")

print(f"{pais_menor_inflacion} es el pais con menor inflacion siendo este de {menor_inflacion}\n")

print(f"{pais_mayor_paro} es el pais con mayor paro siendo este de {mayor_paro}")



#Calculemos el PIB medio, inflación media, paro medio

#Leemos el archivo

archivo = open("Python/day_4/paises.csv")

#Saltamos la primera linea

next(archivo)

total_pib = 0
inflacion_total = 0
paro_total = 0
total_paises = 0

for linea in archivo:

    datos = linea.strip().split(",")

    pais = datos[0]
    pib = float(datos[1])
    inflacion = float(datos[2])
    paro = float(datos[3])

    total_pib += pib
    inflacion_total += inflacion
    paro_total += paro
    total_paises += 1

print(f"PIB medio es {total_pib/total_paises}\n")
print(f"Inflacion media es {inflacion_total/total_paises}\n")
print(f"Paro medio es {paro_total/total_paises}\n")
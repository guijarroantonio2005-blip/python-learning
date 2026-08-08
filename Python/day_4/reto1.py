#Calculamos el PIB total leyendo el archivo

archivo = open("Python/day_4/paises.csv", "r")

next(archivo)

total_pib = 0

for linea in archivo:

    datos = linea.strip().split(",")

    total_pib += float(datos[1])

print(total_pib)
    

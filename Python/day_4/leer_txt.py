archivo = open("Python/day_4/datos.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()



archivo = open("salida.txt", "w")

archivo.write("Hola Mundo\n")
archivo.write("Aprendiendo Python\n")
archivo.write("Data science\n")


archivo = open("Python/day_4/paises.csv", "r")

for linea in archivo:
    print(linea.strip())

archivo.close()

#Separemos las columnas

archivo = open("Python/day_4/paises.csv", "r")

for linea in archivo:
    datos = linea.strip().split(",")

    print(datos)

archivo.close()

#CONVIRTAMOS TIPOS

archivo = open("Python/day_4/paises.csv", "r")

next(archivo) #Saltamos la primera vlinea

for linea in archivo:

    datos = linea.strip().split(",")

    pais = datos[0]
    pib = float(datos[1])
    inflacion = float(datos[2])
    paro = float(datos[3])

    print(f"{pais} tiene un PIB de {pib}")


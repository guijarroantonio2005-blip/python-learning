def cargar_paises(nombre_archivo):

    #Primero cargamos el archivo

    archivo = open(nombre_archivo, "r")

    #Leemos el archivo y lo ponemos en forma de diccionario

    #Creamos el diccionario

    paises = []

    next(archivo)

    for linea in archivo:

        datos = linea.strip().split(",")
        pais ={"pais":datos[0], "pib": float(datos[1]), "inflacion": float(datos[2]), "paro": float(datos[3])}

        paises.append(pais)

    return paises
paises = [
    {"pais": "España", "PIB": 1500, "inflacion": 2.8, "paro": 11.5, "poblacion": 48.6},
    {"pais": "Francia", "PIB": 2800, "inflacion": 2.4, "paro": 7.3, "poblacion": 68.0},
    {"pais": "Alemania", "PIB": 4200, "inflacion": 2.1, "paro": 3.2, "poblacion": 84.4},
    {"pais": "Italia", "PIB": 2100, "inflacion": 1.9, "paro": 7.6, "poblacion": 58.9},
    {"pais": "Portugal", "PIB": 280, "inflacion": 2.5, "paro": 6.1, "poblacion": 10.5},
    {"pais": "Países Bajos", "PIB": 1000, "inflacion": 2.3, "paro": 3.7, "poblacion": 17.9},
    {"pais": "Bélgica", "PIB": 620, "inflacion": 2.2, "paro": 5.6, "poblacion": 11.8},
    {"pais": "Austria", "PIB": 510, "inflacion": 2.0, "paro": 5.2, "poblacion": 9.2},
    {"pais": "Suecia", "PIB": 620, "inflacion": 2.1, "paro": 7.4, "poblacion": 10.6},
    {"pais": "Dinamarca", "PIB": 410, "inflacion": 1.8, "paro": 4.5, "poblacion": 6.0},
    {"pais": "Irlanda", "PIB": 590, "inflacion": 2.7, "paro": 4.2, "poblacion": 5.3},
    {"pais": "Polonia", "PIB": 850, "inflacion": 3.2, "paro": 3.0, "poblacion": 37.8},
    {"pais": "República Checa", "PIB": 340, "inflacion": 2.6, "paro": 2.8, "poblacion": 10.9},
    {"pais": "Grecia", "PIB": 240, "inflacion": 2.9, "paro": 9.8, "poblacion": 10.3},
    {"pais": "Finlandia", "PIB": 320, "inflacion": 1.7, "paro": 7.1, "poblacion": 5.6},
    {"pais": "Reino Unido", "PIB": 3300, "inflacion": 2.9, "paro": 4.3, "poblacion": 68.4},
    {"pais": "Estados Unidos", "PIB": 28700, "inflacion": 2.5, "paro": 4.1, "poblacion": 341.0},
    {"pais": "Canadá", "PIB": 2400, "inflacion": 2.3, "paro": 6.2, "poblacion": 41.0},
    {"pais": "Japón", "PIB": 4200, "inflacion": 1.5, "paro": 2.6, "poblacion": 124.0},
    {"pais": "China", "PIB": 18500, "inflacion": 1.8, "paro": 5.0, "poblacion": 1410.0}
]


def mostrar_paises(lista):
    for pais in lista:
        print(pais)


def buscar_pais(lista, nombre):
    for pais in lista:
        if pais["pais"] == nombre:
            return pais
    return None

def pib_total(lista):
    for pais in lista:
        total += pais["PIB"]
    return total

def inflacion_media(lista):
    i = 0
    for pais in lista:
        total_inflacion += pais["inflacion"]
        i +=1
    return total_inflacion/i

def pais_mayor_pib(lista):
    pais1 = paises[0]
    for pais in paises:
        if pais["PIB"] > pais1["PIB"]:
            pais1 = pais

    return pais1


seleccion = 0

while(seleccion != 5):
    seleccion = int(input("Selecciona entre los siguientes datos que quieras visualizar:\n1. Mostrar países\n2. Buscar país\n3. PIB total\n4. Inflación media\n5. Salir"))
    if seleccion == 1:
        print("Haz seleccionado la opción de mostrar países")
        mostrar_paises(paises)

    if seleccion == 2:
        print("Has seleccionado la opción de buscar país")
        pais = input("¿Qué pais quieres que se muestre en pantalla")
        buscar_pais(paises,pais)

    if seleccion == 3:
        print("El PIB total es: ")
        print(pib_total(paises))

    if seleccion == 4:
        print("La inflación media es: ")
        print(inflacion_media(paises))

    
        

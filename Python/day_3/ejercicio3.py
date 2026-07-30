paises = [
    {"pais":"España","PIB":1500},
    {"pais":"Francia","PIB":2800},
    {"pais":"Alemania","PIB":4200}
]

def obtener_pib_total(lista):
    total = 0
    for pais in lista:
        total += pais["PIB"]
    return total    

resultado = obtener_pib_total(paises)

print(resultado)

#Busquemos un pais

def buscar_pais(lista, nombre):
    for pais in lista:
        if pais["pais"] == nombre:
            return pais
    return None

print(buscar_pais(paises, "España"))    
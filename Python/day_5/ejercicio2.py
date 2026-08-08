from day_4.cargar_datos import cargar_paises
from day_5.ejercicio1 import obtener_pib_total


def obtener_pib_medio(paises):
    pib_total = obtener_pib_total(paises)

    return pib_total / len(paises)


if __name__ == "__main__":
    paises = cargar_paises("day_4/paises.csv")
    print(obtener_pib_medio(paises))
from day_4.cargar_datos import cargar_paises
from day_5.ejercicio1 import obtener_pib_total
from day_5.ejercicio2 import obtener_pib_medio
from day_5.ejercicio3 import pais_mayor_pib
from day_5.ejercicio4 import pais_menor_paro


def resumen_economico(paises):

    print(f"PIB total: {obtener_pib_total(paises)}\n")
    print(f"PIB medio: {obtener_pib_medio(paises)}\n")
    print(f"Pais con mayor PIB: {pais_mayor_pib(paises)}\n")
    print(f"Pais con menor paro: {pais_menor_paro(paises)}")


if __name__ == "__main__":

    paises = cargar_paises("day_4/paises.csv")

    resumen_economico(paises)




#Pais con mayor PIB

from day_4.cargar_datos import cargar_paises

def pais_mayor_pib(paises):

    mayor_pib = 0
    pais_mayor_pib = paises[0]

    for pais in paises:

        if pais["pib"] > mayor_pib:
            mayor_pib = pais["pib"]
            pais_mayor_pib = pais

    return pais_mayor_pib


if __name__ == "__main__":

    paises = cargar_paises("day_4/paises.csv")

    print(pais_mayor_pib(paises))
#Pais con mayor PIB

from day_4.cargar_datos import cargar_paises

def pais_menor_paro(paises):

    menor_paro = 10000
    pais_menor_paro = paises[0]

    for pais in paises:

        if pais["paro"] < menor_paro:
            menor_paro = pais["paro"]
            pais_menor_paro = pais

    return pais_menor_paro


if __name__ == "__main__":

    paises = cargar_paises("day_4/paises.csv")

    print(pais_menor_paro(paises))
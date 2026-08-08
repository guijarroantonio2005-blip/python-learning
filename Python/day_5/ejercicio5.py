#Paises con un paro menor que paro

from day_4.cargar_datos import cargar_paises

def paises_menor_paro(paises, paro):

    paises_menor_paro = []

    for pais in paises:

        if pais["paro"] < paro:

            paises_menor_paro.append(pais)

    return paises_menor_paro


if __name__ == "__main__":

    paises = cargar_paises("day_4/paises.csv")

    print(paises_menor_paro(paises, 8))
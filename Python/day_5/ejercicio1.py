from day_4.cargar_datos import cargar_paises

def obtener_pib_total(paises):

    total_PIB = 0
    for pais in paises:
        total_PIB += pais["pib"]

    return total_PIB


if __name__ == "__main__":
    paises = cargar_paises("day_4/paises.csv")
    print(obtener_pib_total(paises))
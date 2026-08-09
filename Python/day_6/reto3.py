import numpy as np

#Creamos dos arrays
pib = np.array([1500, 2800, 4200, 2100, 280])
paro = np.array([5.2, 7.3, 3.2, 7.6, 6.1])

#Encontremos los PIB de los países cuyo paro sea inferior a 6%.

print(paro < 6)

paro_filtrado = paro < 6
print(pib[paro_filtrado])

#Ahora hagamos lo mismo con el siguiente array
inflacion = np.array([7.8, 5.01, 2.1, 3.01, 9.3])

#Encontremos el PIB de los países cuya inflación sea inferior a 5%.
print(pib[inflacion < 5])
#Veamos el filtrado
import numpy as np

inflacion = np.array([7.8, 5.01, 2.1, 3.01, 9.3])

print(inflacion > 5)
#De esta manera nos devuelve un array con True y False

print(inflacion[inflacion > 5])
#Con [] nos da el array filtrado

print(inflacion[(inflacion > 3) & (inflacion < 6)])

print(inflacion[inflacion > 5].mean())
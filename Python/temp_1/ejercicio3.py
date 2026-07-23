#Veamos cómo utilizamos los inputs
nombre = input("¿Cómo te llamas? ")
#input() lo que va a hacer es pasar ese mensaje a la terminal y tú vas a tener que poner un string
#si lo que queremos es un int o un floar debermos hacer un casting de la siguiente manera
edad = int(input("¿Qué edad tienes?"))
print(f"Hola {nombre}, terminarás la carrera con {edad+3}")
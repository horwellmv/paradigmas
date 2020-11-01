# Manera de leer un archivo que se muestra en memoria.

# archivo = open("texto.txt")
# for linea in archivo:
#     print(linea)


with open ("texto.txt") as archivo:
    for linea in archivo:
        linea = linea.rstrip("/n") # Elimina lo que hay entre parentesis de una cadena
        print (linea)




with open ("Texto1.txt", "w") as archivo2: # Modo escritura, crea si es necesario el .txt - BORRA lo que hay y empieza en blanco. "w+" Me deja leer tambien

    archivo2.write("Gloria Elcy Valencia\n")
    archivo2.write("Fidel Murillo Franco\n")
    archivo2.write("Freiman Savier Murillo Valencia\n")





with open ("texto2.txt", "a") as archivo3: # Modo escritura pero deja lo que habia antes.

    archivo3.writelines(["Este es un nuevo texto ", "Que agrega el modo  -a- "])

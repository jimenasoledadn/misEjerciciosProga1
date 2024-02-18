


nombre = "Juan"
edad = 24
altura = 1.78

print(nombre, edad, altura)

# Otra forma:
print("  1)")
print("Nombre: " + nombre + " Edad: " + str(edad) + " Altura: " + str(altura)) # TODO lo que esta entre comillas es un string

# Otra forma: (Interpolacion--> xq en donde esta la mascara hago que quede el valor)
print("  2)")
print("Nombre: %s Edad: %d Altura: %.2f" %(nombre, edad, altura))

# Otra forma:
print("  3)")
print("Nombre: {} Edad: {} Altura: {}".format(nombre, edad, altura)) # Si no estuvieran en ese orden, se podrian poner numeros. La variable nombre estaria en el lugar 0 --> tendria que ponerlo entre las llaves que estan despues de nombre: {0} . Format analiza el tipo de dato y hace como un str

# Otra forma 2:12 
print("  4)")
print(f"Nombre: { nombre} Edad: { edad } Altura: { altura }") # Entre las llaves puedo poner codigo paython. Tambien x ejemplo puedo poner entre las { 3+9 } una suma y me va a aparecer por consola el resultado
# No usa la funcion python

    #  Secuencias de escape: es cuando en el string quiero que me aparezca COMO CARACTER y NO le de el uso "normal de codigo", x ejemplo, comillas ", uso una LLAVE y luego el CARACTER que deseo que se vea, solo sirve para UN Solo caracter
    
    #  \n --> es para un salto de linea 
    #  \t --> es como una tabulacion
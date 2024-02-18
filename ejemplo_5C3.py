



#variable = 20 # a esta variable al asignarle el numero 20 ya automaticamente se designa el tipo number (si pusiera variable = "20" seria de tipo string)

    # escribo la variable y escribo un punto, me aparecen METODOS/funciones que puedo ejecutar con esa variable entero. Me van a aparecer metodos dependiendo del tipo de la variable

#variable = "hola"

#0print(variable.isdigit()) # IS: son preguntas, ES...? rta es un booleano. En este ejemplo me va a preguntar si dentro de esta cadena TODOS los caracteres son numericos! --> rta: true or false --> FALSE

# La puedo usar para pedir un valor:
        # (Esta solucion es parecida a cuando pedimos validar si un denominador es distinto de cero 
    # while True:
    #     edad = input("Ingrese edad 18-65: ") #Input me devuelve un string

    #     edad = int(edad)

# Esta forma es con validacion (se puede con excepciones)
while True:
    edad = input("Ingrese edad 18-65: ")
    if edad.isdigit(): # Para validar que dentro de la variable edad haya todo numeros, sino marco el error
        edad = int(edad)
        if(edad >= 18 and edad <= 65):
            break
        else:
            print("Edad invalida")
    else:
        print("Eso no es un numero")


print(edad)
print("Fin del programa")
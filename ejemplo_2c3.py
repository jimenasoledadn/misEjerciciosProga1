# Esto se puede hacer porque python es de tipado dinamico, puedo usar el mismo nombre de variable y cambiarle el tipo 

valor = "20" # es una cadena, un string ((si pusiera 2a, en vez de 20**))
print(valor) # aca me va a mostrar el 20, pero de tipo string 

print(type(valor)) # el tipo de la variable valor = "20"

valor = int(valor) # aca cambio el tipo de la variable valor a entero 
print(valor) # aca me va a mostrar el num 20 pero este es de tipo entero
print(type(valor))



    # ** --> Me daria ERROR EN TIEMPO DE EJECUCION: pero cuando llegue a la linea 8, va a encontrarse con una letra (un valor no esperado por la funcion INT, este error es lo que se conoce como EXCEPCION: Se ejecutan las lineas 3 y 4, hasta que en la linea 8 encuentra el error! --> de tipo : ValueError. (SE CUELGA) Se detiene el programa de forma abrupta. Esto es un error del PROGRAMADOR!!!

    # una EXCEPCION solo esta en lenguajes que tienen paradigmas   orientados a objetos
        # una EXCEPCION es un error que lanza un objeto

    # En programacion orientada a objetos TODO es un OBJETO (int, lista, string, float)
        # En este caso el OBJETO seria la funcion INT (en programacion orientada a objetos, los objetos pueden lanzar 2 cosas:
        # . los EVENTOS: ej: el click en un boton, y uno programa la funcion o el codigo que se va a ejecutar luego que se lanza el evento click
        # . las EXCEPCIONES: ej. cada vez que el objeto se encuentra con un error que no sabe como resolverlo (o sea que el programador no predijo como para que se resuelva) nos lanza el error, ejemplo un ValueError)

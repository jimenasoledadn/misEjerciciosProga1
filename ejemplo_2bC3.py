# ME QUEDE EN 1:05 hs.

valor = input("Ingrese un numero: ")

try: 
    valor = int(valor)
    print(valor + 5) # --> se va a ejecutar si no lanza error la linea 6
except ValueError:
    print("Trataste de convertir algo que no es un numero")
# Puedo poner asi para que me aparezca si no hay problemas con el codigo:
# else:
#     print(valor + 5)


# print(valor) --> si dejara esto, se ejecutaria siempre, taaanto si sale bien como si sale mal


    # TRY EXCEPT: 
                #Tengo que cerrar el codigo susceptible a tirar error, en un bloque TRY. Junto con su EXCEPT: en donde vamos a poner que tipo de error vamos a capturar, en este ejemplo es un ERROR DE VALOR: ValueError, y adentro de este bloque escribir el codigo que se va a tener que ejecutar en el caso de que haya aparecido ese error. 
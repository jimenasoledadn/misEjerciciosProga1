# Pedir datos mientras el usuario quiera

#seguir = "s" # inicializo, para que entre por lo menos UNA vez al while

while True:

    try:
        edad = int(input("Ingrese edad 18/65: ")) #--> este es el codigo suceptible de cometer un error
        if( edad >= 18 and edad <= 65):
            break # si el if es valido, va a ir directamente al codigo para mostrar la edad (linea 17)
        else:
            print("Edad invalida")

    except ValueError:
        print("Eso no es un numero")

print(edad)

print("Fin del programa")





    # 1) PRUEBO el while desde un inicio
    # 2) Error EN TIEMPO DE EJECUCION
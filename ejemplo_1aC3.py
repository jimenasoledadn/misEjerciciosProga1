# Pedir datos mientras el usuario quiera

seguir = "s" # inicializo, para que entre por lo menos UNA vez al while

while seguir == "s": # while controlado por la variable seguir

    try:
        edad = int(input("Ingrese edad 18/65: ")) #--> este es el codigo suceptible de cometer un error

    except ValueError:
        print("Eso no es un numero")

    seguir = input("Desea continuar? s/n: ")

print("Fin del programa")





    # 1) PRUEBO el while desde un inicio
    # 2) Error EN TIEMPO DE EJECUCION
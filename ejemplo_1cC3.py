


while True:

    try:
        edad = int(input("Ingrese edad 18/65: ")) #--> este es el codigo suceptible de cometer un error

    except ValueError:
        print("Eso no es un numero")

    else: # aca entra si sale todo bien en el TRY !!! 
        break

print(edad)

print("Fin del programa")
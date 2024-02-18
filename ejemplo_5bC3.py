

while True:
    try:
        edad = int(input("Ingrese edad 18-65: "))
        if(edad >= 18 and edad <= 65):
            break
        else:
            print("Edad invalida")

    except ValueError:
        print("Eso no es un numero")
        

print(edad)
print("Fin del programa")


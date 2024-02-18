# Me quede en 1:36 hs.

resultado = 123 

# NO se podria: xq SOLO se pueden concatenar 2 string !!!
    # --> NO--> print("El resultado es " + resultado) 

try:
    # print("El resultado es " + resultado) # <-- string + number
    print("El resultado es " + str(resultado)) # <-- string + string
except TypeError:
    print("Che NO puedo concatenar int con un string")

# 1)
    # a = 20
    # b = 0 # NO se puede dividir por cero.

    # # rta = a / b --> esta linea me daria error(cuando el denominador es 0)

    # if(b!=0):
    #     rta = a/b
    #     print(rta)
    # else:
    #     print("No se puede dividir por cero")

# 2)
a = 20
b = 0

try: # (intentar/tratar de realizar esta operacion)(aca pongo el cogigo que pueda salir mal)
    rta = a / b
    print(rta)
except ZeroDivisionError: # Puedo poner VARIOS, xq pueden ser varios errores, y que se ejecute un codigo diferente dependiendo de su tipo de error
    print("No esta definido la division por cero")

    # independientemente de si salga bien o mal va a entrar al FINALLY
#finally: --> ejemplo entrar a un archivo, lo haya leido o no, que me deje cerrarlo

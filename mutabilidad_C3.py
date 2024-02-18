            # VARIABLE_ 3 caracteristicas: (2:20:00)

# 1- DIRECCION DE MEMORIA
# 2- TIPO DE DATO
# 3- VALOR
# 4- NOMBRE DE FANTASIA


# EJEMPLO_

x = 20
# 1- DIRECCION DE MEMORIA
print(id(x))
# 2- TIPO DE DATO
print(type(x))
# 3- VALOR
print(x)
# 4- NOMBRE DE FANTASIA : x --> en este caso


# otro EJEMPLO_

x = 40
print(id(x))
print(type(x))
print(x)

    # cada vez que asignamos un nuevo valor a la misma variable, python 
    # INMUTABLE: solamente le podemos dar un valor en el momento en que se creo la variable. Y cuando le queremos asignar otro valor, ese espacio de memoria usado se libera y se busca uno nuevo.   
        # Esto pasa con los Bool, string, int, float

    # LISTAS --> MUTABLE
        # Es parecido al linkedlist
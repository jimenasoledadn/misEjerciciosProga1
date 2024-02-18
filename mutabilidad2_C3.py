# LISTAS --> MUTABLE
        # Es parecido al linkedlist
        # Dentro de las listas puedo poner variables
        # Podemos guardar otras listas, colecciones
        # Esto tmbien corre para js
        # Tienen METODOS (se pone . y aparecen diferentes funciones)
    # Es un elemento ITERABLE. Es lo mismo que me devuelve un range
    # Es DINAMICA: Puedo agregar o quitarle elementos
    # Es MUTABLE: puedo cambiarle el valor a los elementos 
    # Estan INDIZADAS: puedo acceder a cada elemento a traves de su indice que lo identifica 
        # --> ej_ la lista2 tiene 5 elementos --> De LARGO o TAMAÑO : es la cantidad de elementos que estoy guardando en esa lista
        # --> Nunca va a haber un indice igual al tamaño- El indice del ultimo elemento de una lista de tamaño n, es n-1 
        # --> arranco en indice 0 --> el 1 esta en el indice 0
        # SABER! --> lista2 (x ej) --> es la direccion de memoria, y con los [] identifico el elemento a traves de su indice

lista = [] 
lista2 = [1, 3, 2, 5, 8]
lista3 = ["a", "t", "f", "o"]
lista4 = [True, False, False, True, True]
lista5 = [23, "Juan", True, 1.78]
lista6 = [1, 4, 3, 5, ["a", "b", "c", [23, 45, 67, 89]]]

print(lista)
print(lista2)
    # Para MOSTRAR SOLO UN elemento de una lista
print(lista2[0]) # primer elemento
print(lista2[1])
print(lista2[2])
print(lista2[3])
print(lista2[4])
print(lista2[-1]) # = que el indice 4, el elemento 5
print(lista2[-2]) # = que el indice 3, elemento 4
print(lista2[-3]) # = que el indice 2, elemento 3
print(lista2[-4]) # = que el indice 1, elemento 2
print(lista2[-5]) # = que el indice 0, elemento 1
print(lista3)
print(lista4)
print(lista5)
print("\n")
print(lista6)
print(len(lista6))
print(lista6[4]) #para que me muestre el elemento 4--> a su vez este             tiene  4 elementos!!!! 
print(lista6[4][1])
print(lista6[4][3])
print(lista6[4][3][2])
print("\n")
print(type(lista))
print(type(lista2))
print(type(lista3))
print(type(lista4))

print("\n")
    # LEN --> para saber LA CANTIDAD de elementos que tiene una lista:
print(len(lista2))
print("\n")
    # CAMBIAR ej_ de la lista2, el elemento 5 por el 24
lista2[3] = 24 
# Aunque modifique el valor de cualquier elemento, NO CAMBIA la direccion de memoria

    # APPEND _ AGREGAR un elemento a la lista AL FINAL
lista2.append(88)

    # Puedo RECORRER la lista

    # INTERABLE:
print("Iteracion de la lista2: ")
for elemento in lista2: # va a iterar desde 0 a tamaño -1 (sin tener que programarlo). Y la variable ELEMENTO en CADA ITERACION va a guardar el valor de cada uno de los elementos de la lista (en la primer iteracion va  a tener el valor del elemento que esta en el indice 0)
    print(elemento)
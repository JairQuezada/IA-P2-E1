import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#HeapSort usa la lista que creamos previamente para acomodarlas

def heap_sort(lista):
    def heapify(lista, n, i):
        largo = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and lista[i] < lista[l]:
            largo = l
        if r < n and lista[largo] < lista[r]:
            largo = r
        if largo != i:
            lista[i], lista[largo] = lista[largo], lista[i]
            heapify(lista, n, largo)

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n-1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
#En el metodo de Heap sort, se van acomodando por montones, el cual selecciona el maximo de todos los elementos y lo elimina
#Asi consecutivamente hasta que se complete toda la lista
    return lista

lista_nueva = heap_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista completa ya acomodada
import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#QuickSort usa la lista que creamos previamente para acomodarlas

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menor = [x for x in lista[1:] if x <= pivot]
        mayor = [x for x in lista[1:] if x > pivot]
        return quick_sort(menor) + [pivot] + quick_sort(mayor)
#Con quick sort se toma un numero de la lista y va comparando con los otros numeros si son mayor o menor que el numero seleccionado
#y lo va repetiendo hasta que complete toda la lista
lista_nueva = quick_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor    
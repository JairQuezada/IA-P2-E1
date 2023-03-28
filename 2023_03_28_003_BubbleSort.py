import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#BubbleSort usa la lista que creamos previamente para acomodarlas

def bubble_sort(lista):
    largo = len(lista)
    for i in range(largo):
        for j in range(0,largo-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #Este metodo va revisando 1 por 1 y acomoda los numeros con el numero mas cercano, moviendo el menor a la izquierda del mayor
                #esto se hace hasta que se complete la lista entera
    return lista

lista_nueva = bubble_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
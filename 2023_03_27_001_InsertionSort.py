import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#insertionsort usa la lista que creamos previamente para acomodarlas
def insertion_sort(lista):
    for i in range(1, len(lista)):
        numero =  lista[i]
        j=i-1
        #Con la variable numero se guarda el valor el cual se va a acomodar en el futuro
        while j>= 0 and lista[j] > numero:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = numero
        #Se va moviento la variable numero hasta que este sea menor que el numero anterior y luego se inserta el numero
        #Esto se repite varias veces, hasta que se acomoda toda la lista
    return(lista)

lista_nueva = insertion_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
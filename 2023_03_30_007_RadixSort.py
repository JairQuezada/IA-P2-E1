import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#RadixSort usa la lista que creamos previamente para acomodarlas

def radix_sort(lista):
    longitud = len(str(max(lista)))
    
    for digito in range(longitud):
        buckets = [[] for _ in range(10)]
        for numero in lista:
            bucket_index = (numero // 10 ** digito) % 10
            buckets[bucket_index].append(numero)
        lista = [numero for bucket in buckets for numero in bucket]
    return lista
#Este ordena enteros procesando sus digitos individuales el cual lo hace
#Con el bit menos significativo

lista_nueva = radix_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
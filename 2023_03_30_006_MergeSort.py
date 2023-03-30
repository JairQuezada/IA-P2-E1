import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#QuickSort usa la lista que creamos previamente para acomodarlas

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        mitad_Izq = lista[:medio]
        mitad_Der = lista[medio:]
        Izq_Orden = merge_sort(mitad_Izq)
        Der_Orden = merge_sort(mitad_Der)
        return merge(Izq_Orden, Der_Orden)
    
def merge(mitad_Izq, mitad_Der):
    resultado = []
    izquierda = 0
    derecha = 0
    while izquierda < len(mitad_Izq) and derecha < len(mitad_Der):
        if mitad_Izq[izquierda] < mitad_Der[derecha]:
            resultado.append(mitad_Izq[izquierda])
            izquierda += 1
        else:
            resultado.append(mitad_Der[derecha])
            derecha += 1
    resultado += mitad_Izq[izquierda:]
    resultado += mitad_Der[derecha:]
    return resultado
#Con el merge sort se crean varias sublistas, las cuales se van acomodando por menor a mayor, luega esas sublistas se acomoda con las otros sublistas
#Asi repetivamente hasta que se acomoda la lista

lista_nueva = merge_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
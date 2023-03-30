import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#Natura Merge usa la lista que creamos previamente para acomodarlas

def natural_merge_sort(lista):
    if len(lista) <= 1:
        return lista
    def merge(lista1, lista2):
        merged_lista = []
        i, j = 0,0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                merged_lista.append(lista1[i])
                i += 1
            else:
                merged_lista.append(lista2[j])
                j += 1
        merged_lista += lista1[i:] + lista2[j:]
        return merged_lista
    
    runs = []
    start = 0
    while start < len(lista):
        end = start + 1
        while end < len(lista) and lista[end] >= lista[end-1]:
            end += 1
        runs.append(lista[start:end])
        start = end
        
    while len(runs) > 1:
        new_run = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                new_run.append(merge(runs[i], runs[i+1]))
            else:
                new_run.append(runs[i])
        runs = new_run
    return runs[0]
#Esta es similar al Straight Merging, pero este usa subrrays ordenados, esto para optimizar el proceso de ordenamiento

lista_nueva = natural_merge_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
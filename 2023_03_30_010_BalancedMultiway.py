import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#balanced multiway usa la lista que creamos previamente para acomodarlas
m = 2

def balanced_multiway_merge_sort(lista, m):
    n = len(lista)
    if n <= m:
        return sorted(lista)
    else:
        sub_listas = [lista[i:i+m] for i in range(0, n, m)]

        sorted_sub_listas = [balanced_multiway_merge_sort(sub_list, m) for sub_list in sub_listas]

        while len(sorted_sub_listas) > 1:
            new_sorted_sub_listas = []
            for i in range(0, len(sorted_sub_listas), 2):
                if i == len(sorted_sub_listas) - 1:
                    new_sorted_sub_listas.append(sorted_sub_listas[i])
                else:
                    merged_list = merge(sorted_sub_listas[i], sorted_sub_listas[i+1])
                    new_sorted_sub_listas.append(merged_list)
            sorted_sub_listas = new_sorted_sub_listas

        return sorted_sub_listas[0]

def merge(lista1, lista2):
    i, j = 0, 0
    merged_lista = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            merged_lista.append(lista1[i])
            i += 1
        else:
            merged_lista.append(lista2[j])
            j += 1
    merged_lista += lista1[i:]
    merged_lista += lista2[j:]
    return merged_lista

#Este divide la listas en varia sub listas y las ordena poco a poco
lista_nueva = balanced_multiway_merge_sort(lista, m)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
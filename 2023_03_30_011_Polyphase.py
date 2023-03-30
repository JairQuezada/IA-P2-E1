import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#insertionsort usa la lista que creamos previamente para acomodarlas

def polyphase_sort(lista):
    n = len(lista)
    runs = []
    current_run = []
    for i in range(n - 1):
        current_run.append(lista[i])
        if lista[i] > lista[i + 1]:
            runs.append(current_run)
            current_run = []
    current_run.append(lista[n - 1])
    runs.append(current_run)

    k = len(runs)
    while k > 1:
        i = 0
        j = k - 1
        while i < j:
            merged_run = merge_runs(runs[i], runs[j])
            runs.pop(j)
            runs[i] = merged_run
            i += 1
            j -= 1
            if i >= j:
                k = i
    return runs[0]


def merge_runs(run1, run2):
    merged_run = []
    i = 0
    j = 0
    while i < len(run1) and j < len(run2):
        if run1[i] <= run2[j]:
            merged_run.append(run1[i])
            i += 1
        else:
            merged_run.append(run2[j])
            j += 1
    if i < len(run1):
        merged_run.extend(run1[i:])
    else:
        merged_run.extend(run2[j:])
    return merged_run

#Este se usa para ordenar una gran cantidad de datos con archivos
# Pero aqui simulamos estos archivos para lograr acomodar la lista
lista_nueva = polyphase_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
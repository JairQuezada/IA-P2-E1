import random 
lista = [random.randint(0,150)for _ in range(15)]

#Se crea un lista de 15 datos, los cuales gracias al random se sacan listas diferentes cada vez que se ejecuta el programa

print("Esta es la lista que se va a ordenar:   ",lista)
#Distribution of Initial Runs(Dir) usa la lista que creamos previamente para acomodarlas

def dir_sort(lista):
    runs = []
    n = len(lista)
    i = 0
    while i < n:
        run = [lista[i]]
        i += 1
        while i < n and lista[i] >= lista[i-1]:
            run.append(lista[i])
            i += 1
        runs.append(run)
 
    while len(runs) > 1:
        merged_runs = []
        i = 0
        while i < len(runs):
            if i + 1 < len(runs):
                merged_run = merge_runs(runs[i], runs[i+1])
                merged_runs.append(merged_run)
                i += 2
            else:
                merged_runs.append(runs[i])
                i += 1
        runs = merged_runs
 
    return runs[0]
 
def merge_runs(run1, run2):
    merged_run = []
    i = 0
    j = 0
    while i < len(run1) and j < len(run2):
        if run1[i] < run2[j]:
            merged_run.append(run1[i])
            i += 1
        else:
            merged_run.append(run2[j])
            j += 1
    merged_run += run1[i:]
    merged_run += run2[j:]
    return merged_run

#Este divide el array en corridas con el while cuando encuentra un numero menor se agrega a otra lista
#Y se guarda ese dato.
lista_nueva = dir_sort(lista)
print("Esta es la lista ya ordenada: \t\t", lista_nueva)
#Se imprime la lista ya ordenada de menor a mayor
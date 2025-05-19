#1. Remover duplicatas de uma lista
#	•	Crie uma função remover_duplicatas(lista) que:
#	•	Recebe uma lista com elementos repetidos
#	•	Retorna um set com os elementos únicos

#remover_duplicatas([1, 2, 2, 3, 3, 4]) → {1, 2, 3, 4}

def remover_duplicadas (minhaLista):

    my_set = set()
    my_set.update(minhaLista)

    return my_set


lista = [1, 2, 2, 3, 3, 4]
SetResult = remover_duplicadas(lista)

print(SetResult)

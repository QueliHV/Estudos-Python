#1.	Crie uma tupla com 3 números e exiba o maior.

minhatupla = (2,5,8)
print(max(minhatupla))


#2.	Crie uma função que receba uma tupla com 2 números e retorne a média.

def media_tupla(tupla):
    return sum(tupla) / len(tupla)


tupla = (3,7)
media = media_tupla(tupla)

print(media)

#3.	Dada uma tupla de nomes, percorra e imprima com índice:
#Ex: 0 - Queli, 1 - Rafael, etc.

tuplaNomes = ("Queli", "Rafael", "Alice")

print(tuplaNomes)

for item in tuplaNomes:

    indice = tuplaNomes.index(item)
    valor  = item

    if indice == 0:
        linhaRetorno = "0 - " + valor
    else:
        linhaRetorno = linhaRetorno + ", " + str(indice) + " - " + valor

print(linhaRetorno)    

# 4.	Desempacote a tupla (10, 20, 30) em três variáveis e imprima.

tupla4 = (10, 20, 30)
a, b, c = tupla4

print(a, b, c)
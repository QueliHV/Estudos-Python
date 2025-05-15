# 1. Crie uma lista com 5 nomes. Imprima todos em maiúsculo.


minhaLista = ["Queli", "Rafael", "Alice", "Valdete", "José"]

for item in minhaLista:
    print(item.upper())



#2. Peça 5 números ao usuário e armazene numa lista. Depois:
#	•	Mostre a soma
#	•	Mostre o maior e o menor número
#	•	Mostre a média

contador = 0
lista = []

while(contador < 5):
    numeros = input("Digite um número a ser adicionado: \n")
    lista.append(int(numeros))

    contador = contador + 1

print(f"A Lista informada é {lista}")




#3. Crie uma função remover_negativos(lista) que:
#	•	Recebe uma lista de números
#	•	Retorna uma nova lista apenas com números positivos

def remover_negativos(lista):

    listaNova = []

    for item in lista:
        if (item >= 0):
            listaNova.append(item)

    return listaNova
            

lista = [-4, -2, 0, 4, 8]
print(remover_negativos(lista))



#4. Crie uma função contar_letras(lista) que:
#	•	Recebe uma lista de palavras
#	•	Retorna uma nova lista com a quantidade de letras de cada palavra

def contar_letras(listaPalavras):

    listaContador = []

    for item in listaPalavras:
        listaContador.append(len(item))

    return listaContador    


listaPalavras = ["teste","amor", "Festival"]
print(contar_letras(listaPalavras))















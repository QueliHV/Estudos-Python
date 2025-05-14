#1. Soma acumulada com return
#Crie uma função acumular_soma(valor_atual, novo_valor) que:
#	•	Recebe dois inteiros
#	•	Retorna a nova soma acumulada
#total = 0
#total = acumular_soma(total, 5)
#total = acumular_soma(total, 10)
#print(total)  # 15

def acumular_soma(valor_atual, novo_valor):
    return valor_atual + novo_valor

print(acumular_soma(100, 10))

#2. Contar pares em uma lista
#Crie a função contar_pares(lista) que:
#	•	Recebe uma lista de números
#	•	Retorna quantos são pares

def contar_pares(lista):
    contador = 0

    for item in lista:
        if (item % 2 == 0):
            contador = contador + 1

    return contador


lista = [1,2,5,8,11,15,20,24,48]
print(contar_pares(lista))


#3. Adicionar item em uma lista (sem return)
#Crie a função adicionar_item(lista, item) que:
#	•	Recebe uma lista e um item
#	•	Adiciona o item à lista (modificando-a diretamente)
#	•	Imprime a nova lista

def adicionar_item(lista, item):
    lista.append(item)

    
lista = [1,10,20]
adicionar_item(lista, "teste")

print(lista)



#4. Filtrar valores acima da média
#Crie a função acima_da_media(lista) que:
#	•	Recebe uma lista de números
#	•	Retorna uma nova lista contendo apenas os números maiores que a média


def acima_da_media(lista, media):
    listaNew = []

    for item in lista:
        if (item > media):
            listaNew.append(item)

    return listaNew        

lista = [10,20,30,40,50]
media = 35
print(acima_da_media(lista, media))





    







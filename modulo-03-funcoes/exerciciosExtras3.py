#6. Função que calcula a média de notas
#Crie a função calcular_media(lista) que:
#	•	Recebe uma lista de notas
#	•	Retorna a média, com 2 casas decimais


def calcular_media(lista):
    soma = 0

    for item in lista:
        soma = soma + item

    return soma / len(lista)



notas = [10,8.5,5,7]
media = calcular_media(notas)

print(f"A média calculada é {media:.2f}!")


#18.	Use enumerate para imprimir os índices e os valores de uma lista de nomes.
lista_alunos = ["ana", "joao", "maria","pedro","paulo"]

for nome, indice in enumerate(lista_alunos):
	print(f'O Aluno {nome} está na posição {indice}')


 #19.	Use zip para juntar duas listas: nomes e notas de alunos.    
lista_notas = [10,9,8,8,10]
lista_alunos = zip(lista_alunos, lista_notas)
lista_alunos = list(lista_alunos)
print(lista_alunos)


#20.	Use map para dobrar os valores de uma lista de números.
def dobra_numero(numero):
    return numero * 2

lista_numeros = [1,2,4,5,10]
# aplica primeiro parametro para toda a lista
lista_resultado = list(map(dobra_numero, lista_numeros))
print(lista_resultado)


#21.	Use filter para filtrar os números pares de uma lista.
def verifica_pares(numeros):
    return numeros % 2 == 0


numeros_pares = filter(verifica_pares, lista_numeros)
numeros_pares = list(numeros_pares)
print(lista_numeros)
print(numeros_pares)


#22.	Use sorted para ordenar uma lista de dicionários com alunos (chave: nome, nota).

alunos = [{
    "nome" : "Joao",
    "nota" : 10
},
{
    "nome" : "Maria",
    "nota" : 9
},
{
    "nome" : "fernanda",
    "nota": 8
}]

for aluno in alunos:
    print(aluno)
    
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno["nota"])	

print(alunos_ordenados)


    

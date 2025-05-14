#4. Função com for e lista

#Crie uma função chamada exibir_lista(lista) que:
#	•	Recebe uma lista como parâmetro
#	•	Percorre os elementos usando for
#	•	Imprime cada item da lista na tela
#   exibir_lista(["Python", "Java", "C++"])

def exibir_lista(lista):
    for elementos in lista:
        print(elementos)

exibir_lista(["Python", "Java", "C++"])        
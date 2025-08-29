''''
7. Listas, Tuplas e Dicionários
	13.	Crie uma lista com 5 frutas e exiba cada uma usando for.
	14.	Crie uma tupla com os dias da semana e mostre o terceiro dia.
	15.	Crie um dicionário com os dados de um aluno (nome, idade, nota) e imprima os valores.
'''    

lista_frutas = ["uva", "maça", "banana", "laranja","pera"]

for i in lista_frutas:
    print(i)
    
tupla_dias_semana = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sabado", "domingo")
print(tupla_dias_semana[2])


dicionario_alunos = { "nome" : "Joao", "idade" : 20, "nota" : 10}
print(f'O aluno {dicionario_alunos["nome"]} tem {dicionario_alunos["idade"]} e obteve a nota {dicionario_alunos["nota"]}')
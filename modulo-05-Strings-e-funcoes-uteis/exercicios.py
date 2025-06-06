
def estudos_string():
	#Exercicios Strings
	#1.	Receba uma frase do usuário e exiba-a sem espaços no início e no fim.
	frase = input("Digite uma frase: \n")
	print(frase.strip())
		
	#2.	Converta uma string para letras minúsculas e verifique se ela começa com 'python'.
	minhaString = "Python teste letras"
	print(minhaString.lower())
	print(minhaString.startswith("Python"))

	#3.	Conte quantas vezes a letra 'a' aparece em uma string fornecida pelo usuário.
	minhaStringCount = "teste de contagem de letras a"
	print(minhaStringCount.count("a"))

	#4.	Substitua todas as ocorrências da palavra 'ruim' por 'ótimo' em uma frase.
	minhaStringReplace = "Dia hoje está muito ruim"
	print(minhaStringReplace.replace("ruim", "ótimo"))

	#5.	Divida uma frase em palavras e exiba a quantidade de palavras.
	minhaFraseSplit = "Eu gosto de comida italiana com vinho"
	print(len(minhaFraseSplit.split()))


def estudos_lista():	

		
	#1.	Crie uma lista com 5 nomes e adicione um novo nome ao final.
	minhaLista = ["mario", "Joao", "Pedro", "Ana", "Tereza"]
	print(minhaLista)
	minhaLista.append("Queli")
	print(minhaLista)


	#2.	Remova o terceiro item de uma lista qualquer e imprima a nova lista.
	minhaLista.remove(minhaLista[2])
	print(minhaLista)
	

	#3.	Ordene uma lista de números e exiba o maior e o menor valor.
	minhaLstaOrdenadaNumeros = [10,20,30,1,9,5,0]
	minhaLstaOrdenadaNumeros.sort()
	print(minhaLstaOrdenadaNumeros)
	print(f"Maior: {max(minhaLstaOrdenadaNumeros)} e Menor: {min(minhaLstaOrdenadaNumeros)}")
	

	#4.	Utilize o método pop() para remover o último elemento e exiba-o.
	minhaListaPop = ["a", "b", "c", "d"]
	minhaListaPop.pop()
	print(minhaListaPop)
	

	#5.	Some todos os elementos de uma lista numérica.
	minhaListaSoma = [10, 20, 30, 40, 50]
	print(minhaListaSoma)
	soma = sum(minhaListaSoma)
	print(soma)


def estudos_list_comprehension():
	print("estudos_list_comprehension")

	#1.	Crie uma lista com os quadrados dos números de 0 a 10.
	listaQuadrados = [numero **2 for numero in range(0,11)]
	print(listaQuadrados)
	


	#2.	Crie uma lista com apenas os números pares de 0 a 20.
	listaPares = [numero for numero in range(0,21) if numero % 2 == 0]
	print(listaPares)
	

	#3.	A partir de uma lista de nomes, crie uma nova lista apenas com os nomes que começam com 'A'.
	listaNomes = ["Amanda", "Carlos", "Ana", "João", "Alberto", "Queli", "Alice"]
	listaNomesA = [nome for nome in listaNomes if nome.lower().startswith("a")]
	print(listaNomesA)
	


	#4.	Crie uma lista com o dobro de cada número de uma lista dada.
	listaOrigem = [10,15,13,20,5]
	listaDobro = [numero*2 for numero in listaOrigem]
	print(listaDobro)
	


	#5.	Transforme uma lista de strings em uma lista com o comprimento de cada string.	
	listaStrings = ["casa", "teste", "rua", "amor"]
	listaTamanhoStrings = [len(palavra) for palavra in listaStrings]
	print(listaTamanhoStrings)



def funcoes_auxiliares():

	#1.	Use enumerate() para exibir os índices e nomes de uma lista de alunos.
	listaNome = ["Ana", "Jose", "Maria", "Pedro", "Carlos"]

	for indice, nome in enumerate(listaNome):
		print(f"Exerc1 - Indice: {indice} - Nome: {nome}")

	#2.	Use zip() para juntar duas listas: nomes e idades, e exiba pares nome-idade.
	listaIdade = [30,40,24,50,18]
	resuldado = zip(listaNome, listaIdade)
	print(list(resuldado))
	

	#3.	Use map() para converter uma lista de strings numéricas para inteiros.
	listaStrings = ["1","5","4","6","10"]
	listaNumerica = map(lambda x:int(x), listaStrings)
	print(list(listaNumerica))
	
	#4.	Use filter() para filtrar os números maiores que 10 de uma lista.
	listaNumeros = [1,3,10,20,45,60]
	listaFiltrada = filter(lambda x:x > 10, listaNumeros) #Envia cada numero da lista para a função
	print(list(listaFiltrada))
	
	#5.	Use lambda com sorted() para ordenar uma lista de dicionários por um campo 'idade'.
	meuDicionario = [
		{
		'nome' : "Queli",
		'idade' : 39
		},
		{
			'nome' : "Rafael",
			'idade' : 43
		},

		{'nome' : "Alice",
   		 'idade' : 3}
	]

	meuDicOrdenado = sorted(meuDicionario, key=lambda pessoa: pessoa['nome'])
	print(meuDicOrdenado)



def fatiamento():
	#1.	Exiba os 3 primeiros caracteres de uma string.
	minhaString = 'fatiamento'
	print(minhaString[0:3])  # maior ou igual ao primeiro parametro e menor que o segund (indice)

	#2.	Mostre os 2 últimos elementos de uma lista com pelo menos 4 itens.
	minhaLista = ['teste', 20, True, 'Queli', 10]
	print(minhaLista[(len(minhaLista) - 2):len(minhaLista)])

	#3.	Inverta uma string usando slicing.
	minhaString = "Amor"
	print(minhaString[::-1])

	#4.	Crie uma sublista com os elementos nas posições pares de uma lista.
	minhaStringPar= minhaString[::2]
	print(minhaStringPar)
	
	#5.	Exiba uma string ignorando os 2 primeiros e os 2 últimos caracteres.
	print(minhaString[1:-1:])


def exibeMenu():

	while True:

		print("============ MENU ============")
		escolha = int(input("1 - Estudos Strings \n2 - Estudos Lista \n3 - Estudos List Comprehension \n4 - Funções Auxiliares \n5 - Fatiamento \n6 - Sair \n"))

		if escolha == 1:
			estudos_string()
			
		elif escolha == 2:
			estudos_lista()	
			
		elif escolha == 3:
			estudos_list_comprehension()
			
		elif escolha == 4:
			funcoes_auxiliares()
			
		elif escolha == 5:
			fatiamento()
			
		elif escolha == 6:
			break
		else:
			print("Opção Inválida, escolha uma das opções abaixo \n")	


exibeMenu()















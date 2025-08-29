''''
8. Strings e Funções Úteis
	16.	Peça uma frase ao usuário e imprima:

	•	A frase em letras maiúsculas
	•	A quantidade de caracteres
	•	Se ela contém a palavra “Python”

17.	Faça um programa que leia um nome completo e exiba apenas o primeiro nome.

'''

def verifica_frase(frase):
	print(frase.upper())
	print(len(frase))

	palavra = frase.find("Python")

	if (palavra != -1):
		print("Localizou a palavra Python")
	else:
		print("Não localizou a palavra Python")	

def imprime_primeiro_nome(nome_completo):
	palavras = nome_completo.split()
	print(f'O primeiro nome é {palavras[0]}')
					

frase = input("Digite uma frase: \n" )
verifica_frase (frase)

nome_completo = input("Digite seu nome completo: \n")
imprime_primeiro_nome(nome_completo)


'''
🔹 1. Variáveis e Tipos de Dados
	1.	Crie variáveis para armazenar seu nome, idade e se você está estudando Python. 
    Exiba essas informações no console.
	2.	Converta uma string para inteiro e faça uma soma com outro número inteiro.
	3.	Escreva um programa que calcule o IMC a partir do peso e altura do usuário.
'''

nome = "Queli"
idade = 40
estudando_python = True

print(f'Me chamo {nome}, tenho {idade} e estou estudando python')

numero_1 = "10"
numero_2 = 25
numero_3 = 30

soma = int(numero_1) + numero_2 + numero_3
print(soma)


peso = float(input("Informe seu peso: \n"))
altura = float(input("informe sua altura: \n")) / 100

print(peso, altura)

imc = peso / (altura * altura)

print(imc)
print(f"Seu Imc é {imc:.2f}")

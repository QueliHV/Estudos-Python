'''
3. Operadores e Expressões
	5.	Escreva um programa que receba dois números e mostre:
	•	A soma
	•	A subtração
	•	O produto
	•	A divisão
'''

num1 = float(input("Informe o primeiro número: \n"))
num2 = float(input("Informe o segundo número: \n"))

soma = num1 + num2
subtracao = num1 - num2
produto = num1 * num2
divisao = num1 / num2

print(f'Soma: {soma} \nSubstração: {subtracao} \nProduto: {produto} \nDivisão: {divisao:.2f}')
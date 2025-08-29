''''
4. Estruturas Condicionais
	6.	Verifique se um número é positivo, negativo ou zero.
	7.	Peça a idade do usuário e diga se ele é menor de idade, adulto ou idoso.
	8.	Escreva um programa que verifique se um número é par ou ímpar.
'''

numero = int(input("Informe um número \n"))

if (numero > 0):
    print("Esse número é positivo")
elif(numero < 0):
    print("Esse número é negativo")
else:
    print("Esse número é igual a zero")    


idade = int(input("Informe sua idade: \n"))

if (idade < 18):
    print("Você é menor de idade")
elif(idade >= 18 and idade < 60):
    print("Você é adulto")   
else:
    print("Você é idoso")


numero_verificado = int(input("Informe um número para verificação: \n"))
if (numero_verificado % 2 == 0):
    print("Este é um número par!")
else:
    print("Esse é um número impar!")    



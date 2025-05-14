#	1.	Crie as variáveis:
#	•	nome (str)
#	•	idade (int)
#	•	altura (float)
#	•	Exiba uma frase como:  "Olá, meu nome é Queli, tenho 39 anos e 1.65m de altura."


nome = "Queli"
idade = 39
altura = 1.63

print(f"Olá, meu nome é {nome}, tenho {idade} e {altura} de altura.")



#2.	Mostre o tipo de cada variável usando type(). Exemplo: print(type(nome))  # <class 'str'>

print(type(nome))
print(type(idade))
print(type(altura))

#3.	Calcule o IMC, criando uma variável peso (float):
#Fórmula: IMC = peso / (altura ** 2)

peso = 68
imc = peso / (altura ** 2)

print(f"Seu imc é {imc:.2f}")


#	5.	Use os operadores //, % e ** em exemplos simples.

print(10 // 3)  # Divisão inteira
print(10 / 3) # Divisão
print(10 % 3) # resto
print(3**3) # elevado




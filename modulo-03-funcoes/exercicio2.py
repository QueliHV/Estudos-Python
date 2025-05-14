#2. Função com parâmetros e retorno

#Crie uma função chamada calcular_imc(peso, altura) que:
#	•	Recebe dois parâmetros: peso (float) e altura (float)
#	•	Retorna o IMC, que é calculado com a fórmula: IMC = peso / (altura ** 2)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = 68
altura = 1.63

imc = calcular_imc(peso, altura)
print(f"O IMC é {imc:.2f}")


# Crie um programa com as seguintes etapas:
	
#1.	Peça ao usuário nome, idade e valor de saque.
#2.	Se a idade não for número → trate com ValueError.
#3.	Crie uma exceção personalizada chamada ErroLimiteSaque.
#4.	Se o valor do saque for maior que 500 → dispare ErroLimiteSaque.
#5.	Use finally para exibir “Operação finalizada”.

class ErroLimiteSaque(Exception):
    pass

class erroNomeVazio(Exception):
    pass

while True:
    try:
        nome = input("Digite seu nome:  \n")

        if nome == "":
            raise erroNomeVazio ("Nome inválido, informe novamente!")

        break

    except erroNomeVazio as e:
        print (e)
        


while True:
    try:
        idade = int(input("Digite sua idade: \n"))
        break
    except ValueError:
        print("Idade Inválida, por favor digite um número!")    


while True:
    try:
        valor_saque = float(input("Digite o valor do saque: \n"))
        
        if (valor_saque > 500):
            raise ErroLimiteSaque        
        break
        
    except ValueError:
        print("Valor Saque Inválido. Digite um número válido")

    except ErroLimiteSaque as e:
        print("Valor Saque Inválido. Digite um valor menor ou igual a 500")
    


print ("Operação finalizada.")
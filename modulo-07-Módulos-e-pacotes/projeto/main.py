from validacoes import valida_idade, valida_nome

while True:
    nome = input("Informe seu nome: ")

    if valida_nome(nome):
        print("Nome Válido")
        break
    else:
        print("Nome Inválido")    


while True:

    try:
        idade = int(input("Informe sua idade: "))
        break
    except ValueError:
        print("Idade Inválida")        

if valida_idade(idade):
    print("Idade válida")
else:
    print("Idade Inválida")            
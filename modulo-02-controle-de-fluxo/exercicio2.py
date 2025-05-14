# 2.	Crie uma senha definida no código. Peça ao usuário para digitar a senha correta com no 
# máximo 3 tentativas (while ou for).

senha = "Abc123@"
tentativa = 0

while tentativa < 3:   # começa em zero
    senhaUser = input("Informe a senha:")
    acertou = senhaUser == senha
    tentativa = tentativa + 1


    if (acertou):
        print("Senha correta!")
        break
    elif (tentativa > 3):
        print("Número de tentativas excedido!")
        break
    else:
        continue
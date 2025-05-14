#5. Função que imprime um menu interativo
#
#Crie a função mostrar_menu() que:
#	•	Exibe opções no terminal (como um sistema simples)
#	•	Usa while e input() para repetir até a pessoa digitar “0”

# Exemplo de uso:
#mostrar_menu()
# Exibe:
# 1 - Adicionar
# 2 - Remover
# 0 - Sair

def mostra_menu():

    escolha = input("Escolha uma das opções: \n1 - Adicionar \n2 - Remover \n0 - Sair \n")
    
    while(int(escolha) != 0):
        escolha = input("Escolha uma das opções: \n1 - Adicionar \n2 - Remover \n0 - Sair \n")

    return escolha

mostra_menu()

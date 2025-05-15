#Objetivo:

#Permitir ao usuário:
#	1.	Adicionar produtos
#	2.	Listar produtos
#	3.	Ver total geral do catálogo
#	4.	Sair


catalogo = []
produto = {
    "nome" : "Mouse",
    "preco" : 50.0
}


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    produto = {
        "nome" : nome,
        "preco" : preco
    }

    catalogo.append(produto)
    print("Produto Adicionado!")


def listar_produtos():    
    if not catalogo:
        print("Nenhum produto cadastrado!")
        return
    
    for produto in catalogo:
        print(f"{produto['nome']} - R$ {produto['preco']:.2f}")


def ver_total_catalogo():

    total = sum(produto["preco"] for produto in catalogo)
    print(f"Total dos produtos: RS {total:.2f}")

    

def mostrar_menu():

    while(True):
        print("===== MENU =====")
        print("1 - Adicionar Produto")
        print("2 - Lista Produtos")
        print("3 - Ver total do catalogo")
        print("0 - Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            adicionar_produto()
        elif escolha == 2:
            listar_produtos()
        elif escolha == 3:
            ver_total_catalogo()
        elif escolha == 0:
            print("Saindo do sistema, até logo!")
            break
        else:
            print("Opção Inválida!")


mostrar_menu()    


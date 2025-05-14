#Crie uma função acumuladora de compras:
# A cada chamada, adiciona um item à lista de compras
# Exibe o total e os itens




def acumula_compra (lista, novoItem):
    lista.append(novoItem)


somaLista = 0
lista = []
escolha = ""

while escolha != "9":

    escolha = input("Digite um item ou 9 para finalizar a lista: \n")

    if (escolha == "9"):
        break

    acumula_compra(lista, escolha)
    valor = float(input("Digite o valor: \n"))
    somaLista = somaLista + valor


print(f"Esse é o total da sua compra: {somaLista} e essa é a sua lista {lista}")




    



def criaNovoArquivo(pathArquivo, pathArquivoNovo):

    # Le arquivo e grava conteudo e variavel
    with open(pathArquivo, "r") as arquivo:
        arquivoNovo = arquivo.read()

    # escreve e outro arquivo com conteudo lido anteriormente
    with open(pathArquivoNovo, "w") as arquivo:
        arquivo.write(arquivoNovo)    


def eliminaArquivo(pathArquivo):

    # Le arquivo e passa branco
    with open(pathArquivo, "w") as arquivo:
        arquivo.write("")



#1.	Escreva 5 nomes em um arquivo .txt, um por linha.

with open("arquivos/arquivo-txt.txt", "w") as arquivo:
    arquivo.write("Queli \n")
    arquivo.write("Rafael \n")
    arquivo.write("Alice \n")
    arquivo.write("João \n")
    arquivo.write("Maria \n")

#2.	Leia o conteúdo e exiba os nomes com numeração.
with open("arquivos/arquivo-txt.txt", "r") as arquivo:
    arquivoLido = arquivo.readlines()

    for indice, elemento in enumerate(arquivoLido):
        print(f"{indice} - {elemento}")


#3.	Adicione um novo nome ao final do arquivo.
with open("arquivos/arquivo-txt.txt", "r+") as arquivo:
    conteudo = arquivo.read()
    arquivo.write("Ana")


#4.	Crie uma função para apagar todo o conteúdo do arquivo.
pathArquivoOrig = "arquivos/arquivo-txt.txt"
pathArquivoNovo = "arquivos/arquivo2-txt.txt"
criaNovoArquivo(pathArquivoOrig, pathArquivoNovo)
eliminaArquivo(pathArquivoNovo)


#5.	Mostre quantas linhas o arquivo possui.
with open(pathArquivoOrig, "r") as arquivo:
    arquivoLido = arquivo.read()
    numeroLinhas = arquivoLido.count('\n') + 1
    print(numeroLinhas)
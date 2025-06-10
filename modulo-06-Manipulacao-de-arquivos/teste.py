
# Modo R = abrir arquivo em modo read (somente leitura)
'''
with open("arquivos/dados_teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

with open("arquivos/dados_teste.txt", "r") as arquivo:
    conteudoLinha = arquivo.readlines()
    
for linha in conteudoLinha:
    print(linha)
'''

# Modo W = Abre/ cria arquivo e insere dados (se ja existir apaga conteudo)
with open("arquivos/dados_write.txt", "w") as arquivo:
    arquivo.write("teste de write - linha 1\n")
    arquivo.write("teste de write  - linha 2\n")



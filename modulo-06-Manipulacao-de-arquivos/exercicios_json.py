# Escrevendo dados em um json

'''
dados = {
    "nome" : "Queli",
    "idade" : 40,
    "notas" : [10.0, 8.0, 9.5]
}

with open ("arquivos/dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4 )


# Lendo dados de um json   

with open("arquivos/dados.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
print(type(dados))

# Converte para string
dados_string = json.dumps(dados, indent=4)
print(dados_string)
print(type(dados_string))

# converte para dicionário
dados_dict = json.loads(dados_string)
print(dados_dict)
print(type(dados_dict))
'''

import json


# 1. Criar e salvar um dicionário em um arquivo JSON
# Objetivo: Crie um dicionário com dados de um aluno e salve em um arquivo chamado aluno.json.
# {"nome": "Queli", "idade": 39, "notas": [9.5, 8.0, 10.0]}

aluno = {
    "nome" : "Queli",
    "idade" : 39,
    "notas" : [9.5, 8.0, 10.0]
}

print(aluno)

with open("arquivos/aluno.json", "w") as arquivo:
    json.dump(aluno, arquivo, indent=4 )


# 2. Ler o arquivo JSON e exibir os dados no terminal
# Objetivo: Leia o arquivo aluno.json e exiba os dados com formatação:
# Nome: Queli | Idade: 39 | Notas: 9.5, 8.0, 10.0

with open("arquivos/aluno.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
# Junta o conteudo separado por ','  e converte para elemento para string
notas = ', '.join(str(nota) for nota in dados['notas'])  
print(f"Nome : {dados['nome']} | Idade: {dados['idade']} | Notas : {notas}")    



# 3. Adicionar um novo campo ao JSON existente
# Objetivo: Adicione o campo "aprovado": True ao JSON já existente e salve novamente no mesmo arquivo.

with open("arquivos/aluno.json", "r") as arquivo:
    aluno_alterado = json.load(arquivo)

aluno_alterado['aprovado'] = True
print(aluno_alterado)    



# 4. Salvar uma lista de dicionários (vários alunos) em um novo arquivo JSON
# Objetivo: Crie uma lista com 3 alunos (cada um com nome, idade e notas) e salve no arquivo alunos.json.

lista_alunos = []

aluno1 = {
    "nome" : "Queli",
    "idade" : 40,
    "notas" : [10.0, 9.5, 8.5]
}

lista_alunos.append(aluno1)

aluno2 = {
    "nome" : "Rafael",
    "idade" : 43,
    "notas" : [8.0, 9.8, 8.5]
}

lista_alunos.append(aluno2)

aluno3 = {
    "nome" : "Alice",
    "idade" : 3,
    "notas" : [9.5, 10, 7.8]
}

lista_alunos.append(aluno3)

print(lista_alunos)

with open ("arquivos/lista_alunos.json", "w") as arquivo:
    json.dump(lista_alunos, arquivo, indent=4)



# 5. Ler o arquivo alunos.json e exibir a média de notas de cada aluno
# Objetivo: Para cada aluno do arquivo alunos.json, calcule e exiba:

with open("arquivos/lista_alunos.json", "r") as arquivo:
    lista_alunos_media = json.load(arquivo)

for aluno in lista_alunos_media:
    media = sum(aluno['notas']) / len(aluno['notas'])
    print(f'Nome : {aluno['nome']} - Média : {media:.2f}')
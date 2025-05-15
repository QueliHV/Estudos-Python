#5. Crie um dicionário com dados de uma pessoa:
#	•	nome, idade, profissão
#	•	Imprima as chaves, valores e pares


pessoa = {
    "nome" : "Queli",
    "idade" : 39,
    "profissao" : "Desenvolvedora de Software"
}

print(pessoa)


#6. Crie uma função resumo_pessoa(pessoa) que:
#	•	Recebe um dicionário com os dados de uma pessoa
#	•	Imprime algo como:
#Nome: João
#Idade: 30
#Profissão: Engenheiro



def resumo_pessoa(pessoa):

    for chave, valor in pessoa.items():
        print(f"{chave} : {valor}")
    
resumo_pessoa(pessoa)    



#7. Crie uma função media_aluno(dados) que:
#	•	Recebe um dicionário com notas:

#dados = {
#    "nome": "Lucas",
#    "notas": [7.5, 8.0, 6.5]
#}

#Calcula e retorna a média

def media_aluno(dados):
    for chave, valor in dados.items():

        if chave == "notas":
            media = sum(valor) / len(valor)
            
    return media

    

dados = {
    "nome" : "Lucas",
    "notas" : [7.5, 8.0, 6.5]
}        

media = media_aluno(dados)
print(f"A média do aluno é {media:.2f}")


import csv

def exercicio1():

    # 1. Criar um arquivo CSV
    '''
    Crie um arquivo alunos.csv com os seguintes dados:

    nome  idade nota
    Queli  39    9.5
    Rafael 40    8.0
    Alice   3   10.0

    Use csv.DictWriter.
    '''   
    
    with open ("arquivos/alunos.csv", "w", newline='') as arquivo:
        campos = ["nome", "idade", "nota"]  #cabeçalho (fildnames)
        escritor = csv.DictWriter(arquivo, fieldnames=campos) #escreve cabeçalho

        escritor.writeheader ()
        escritor.writerow({"nome" : "Queli", "idade" : 39, "nota" : 9.5})
        escritor.writerow({"nome": "Rafael", "idade" : 43, "nota" : 8.0})
        escritor.writerow({"nome" : "Alice", "idade" : 3, "nota" : 10.0})


def exercicio2():        

    # 2. Ler o arquivo CSV
    # Leia o arquivo alunos.csv e exiba as informações de cada aluno no seguinte formato: 
    # Nome: Queli | Idade: 39 | Nota: 9.5

    with open("arquivos/alunos.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)  # Cada linha se torna um adicionario

        for dicionario in leitor:
            nome = dicionario["nome"]
            idade = dicionario["idade"]
            nota = dicionario["nota"]

            print(f"Nome: {nome} | Idade: {idade} | Nota: {nota}")


def exercicio3():

    #Adicione um novo aluno ao arquivo existente, sem apagar os dados anteriores:      
    # nome: João
    # idade: 28
    # nota: 7.0      

    nomeColunas = ['nome', 'idade', 'nota']
    dadosColunas = {"nome": "João", "idade": 28, "nota": 7.0}


    with open("arquivos/alunos.csv", "a", newline='') as arquivo:
        
        escritor = csv.DictWriter(arquivo, fieldnames=nomeColunas)
        escritor.writerow(dadosColunas)


def exercicio4():       

    #4. Calcular média das notas
    #Leia todas as notas do arquivo CSV e calcule a média geral da turma.   

    totalNotas = 0
    qtAlunos = 0

    with open("arquivos/alunos.csv", "r", newline='') as arquivo: #abre arquivo
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:

            nota = float(aluno["nota"])
            totalNotas += float(aluno["nota"])
            qtAlunos += 1
            

        media = totalNotas / qtAlunos
        print(f"A média geral da turma é {media:.2f}")



def exercicio5():

    # Filtrar alunos com nota maior ou igual a 9  
    with open("arquivos/alunos.csv", "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if float(linha["nota"]) >= 9:
                print(linha)

        

exercicio5()    



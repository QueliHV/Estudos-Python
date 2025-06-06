#Objetivo:
#Permitir que o usuário cadastre alunos com nome e três notas, e ao final, gerar uma lista com a média de cada aluno.

def cadastrar_aluno():

    alunos = []

    while(True):

        try:
            nome = input("Informe o nome do aluno: \n")
            nota1 = float(input("Informe a primeira nota: \n"))
            nota2 = float(input("Informe a segunda nota: \n"))
            nota3 = float(input("Informe a terceira nota: \n"))
            
            media = (nota1 + nota2 + nota3) / 3    

            aluno = {
                    "nome": nome,
                    "nota1" : nota1,
                    "nota2" : nota2,
                    "nota3" : nota3,
                    "media" : media
                }
            
            alunos.append(aluno)

            while(True):

                escolhaCadastro = input("1 - Cadastrar mais alunos \n2 - Voltar ao menu anterior \n")

                if escolhaCadastro == "1":
                    break
                elif escolhaCadastro == "2":
                    return alunos
                else:
                    print("Opção Inválida!")

                   

        except ValueError:
            print("Favor informar somente valores validos para as notas!")
            


        
def consultar_aluno(listaAlunos):
    nome = input("Digite o nome do aluno que deseja consultar: \n")

    # Busca pelo nome considerando sempre com letra minuscula
    alunoSelecionado = [aluno for aluno in listaAlunos if aluno['nome'].lower() == nome.lower()]

    if alunoSelecionado:
        print(f"Nome: {alunoSelecionado[0]['nome']}, Notas: {alunoSelecionado[0]['nota1']} - {alunoSelecionado[0]['nota2']} - {alunoSelecionado[0]['nota3']}, Média: {alunoSelecionado[0]['media']:.2f}")
    else:
        print("Aluno Não Cadastrado!")

    while(True):
        print("Escolha uma das opções para seguir:")
        escolha = input("1 - Voltar ao menu inicial \n2 - Encerrar programa")

        if escolha == "1":
            break
        elif escolha == "2":
            return False
        else:
            print("Opção Inválida!")
                       

def listar_alunos(listaAlunos):

    if(len(listaAlunos) == 0):
        print("Nenhum aluno Cadastrado!")
        return
    else:
        for aluno in listaAlunos:
            print(f"Nome: {aluno['nome']}, Notas: {aluno['nota1']} - {aluno['nota2']} - {aluno['nota3']} - {aluno['media']:.2f}")
            
    while(True):
        print("Escolha uma das opções para seguir:")
        escolha = input("1 - Voltar ao menu inicial \n2 - Encerrar programa \n")

        if escolha == "1":
            break
        elif escolha == "2":
            return False
        else:
            print("Opção inválida!")
    


def mostrar_menu():

    todosAlunosCadastrados = []
    
    while(True):
        print("======= CADASTRO DE ALUNOS =======")
        print("Escolha uma das opções abaixo:")

        escolha = input("1 - Cadastrar Aluno \n2 - Consultar Aluno \n3 - Listar Alunos \n4 - Sair \n")

        if (escolha == "4"):
            return False
        elif (escolha == "1"):
            novosAlunosCadastrados = cadastrar_aluno()
            todosAlunosCadastrados.extend(novosAlunosCadastrados)

        elif (escolha == "2"):
            if consultar_aluno(todosAlunosCadastrados) == False:
                break
        elif (escolha == "3"):
            if listar_alunos(todosAlunosCadastrados) == False:
                break
        else:    
            print("Opção Invalida, escolha uma das opções abaixo:")    
        
        

mostrar_menu()

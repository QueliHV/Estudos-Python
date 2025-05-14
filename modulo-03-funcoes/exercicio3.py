#3. Função com retorno booleano

#Crie uma função chamada eh_par(numero) que:
#	•	Recebe um número como parâmetro
#	•	Retorna True se for par, False se for ímpar



def eh_par(numero):
    return numero % 2 == 0
        
print(eh_par(9))    
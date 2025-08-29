''''
6. Funções
	11.	Crie uma função que receba um nome e imprima uma saudação.
	12.	Crie uma função que receba dois números e retorne a média.
'''

def saudacao (nome):
    print(f'Bom dia {nome}')
    
saudacao("Queli")


def media(num1, num2):
    return (num1 + num2) / 2

print(media(5,10))
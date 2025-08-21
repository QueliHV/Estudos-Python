'''
Sistema de Produto com Estoque Controlado

Crie uma classe chamada Produto com os seguintes atributos e comportamentos:

Atributos:
	•	nome (público)
	•	preco (privado)
	•	estoque (privado)

Métodos:
	•	@property preco: retorna o preço atual.
	•	@preco.setter: atualiza o preço, mas somente se o novo preço for maior que zero.
	•	@property estoque: retorna o estoque atual.
	•	@estoque.setter: atualiza o estoque, mas não permite valor negativo.
	•	vender(qtd): diminui a quantidade em estoque se houver quantidade suficiente.
	•	repor(qtd): aumenta o estoque com a quantidade informada.
'''

class produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.__preco = preco
        self.__estoque = estoque

    @property 
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if (valor <= 0):
            print("Preço deve ser maior que zero!")
        else:
            self.__preco = valor  

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque (self, quantidade):
        if quantidade < 0:
            print("Estoque deve ser maior que zero!")
        else:
            self.__estoque = quantidade


    def vender (self, qtd):
        if (qtd > self.__estoque):
            print("Estoque insuficiente para venda!")
        else:
            self.__estoque -= qtd


    def repor (self, qtde):
        self.__estoque += qtde



p = produto("caneta", 5.00, 10)
print("Dados Caneta: ", p.nome, p.estoque, p.preco)    

p.preco = 8.00
print("Preco caneta ajustado: ", p.preco)

p.estoque = 1
print("Estoque caneta ajustado: ", p.estoque)


p.vender(15)
p.repor(8)

print("Dados Caneta: ", p.nome, p.estoque, p.preco)    






                          
'''
Etapa 1 – Criar Classes e Objetos
	1.	Classe Pessoa
	•	Crie uma classe chamada Pessoa.
	•	A classe deve ter os atributos: nome e idade.
	•	Crie um método apresentar() que exibe:
"Olá, meu nome é {nome} e tenho {idade} anos."
	•	Instancie 2 objetos e chame o método.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')


#p1 = Pessoa("Queli", 40)
#p1.apresentar()  

#p2 = Pessoa("Alice", 3)
#p2.apresentar()  


'''
Etapa 2 – Atributos Privados e Métodos Get/Set
	2.	Classe ContaBancaria
	•	Atributos: titular, saldo (privado).
	•	Métodos:
	•	depositar(valor)
	•	sacar(valor)
	•	ver_saldo() → retorna o saldo.
	•	Faça validações para não permitir saque maior que o saldo.
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Valor Inválido para saldo!")
        else:
            self.__saldo = valor

    

c = ContaBancaria("Queli", 1000)        
#print("Saldo atual: ", c.saldo)

c.saldo = 5000
#print("Saldo atual: ", c.saldo)


'''
Etapa 3 – Construtores e Métodos
	3.	Classe Livro
	•	Atributos: titulo, autor, paginas.
	•	Método detalhes() → imprime uma frase com as informações do livro.
	•	Crie 2 objetos diferentes e chame o método.
'''


class livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        print("Informações do Livro: ", self.titulo, self.autor, self.paginas)


l1 = livro("livro1", "autor1", 100)    
l2 = livro("livro2", "autor2", 200)
    
#l1.detalhes()
#l2.detalhes()


'''
Etapa 4 – Herança
	4.	Classe Base: Funcionario
	•	Atributos: nome, salario.
	•	Método: exibir_dados()
Classe Derivada: Gerente
	•	Herda de Funcionario.
	•	Novo atributo: departamento.
	•	Sobrescreva o método exibir_dados() para incluir o departamento.
'''



class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"O Funcionário {self.nome} tem o salario de {self.salario:2f} ")


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento


    def exibir_dados(self):
        super().exibir_dados()   
        print(f"O departamento do funcionario é o {self.departamento}")


#f1 = Gerente("João", 1200, "TI")
#f1.exibir_dados()


'''
Etapa 5 – Polimorfismo
	5.	Classe Base: Animal
	•	Método falar(), que imprime "Som genérico".
Classes Derivadas: Cachorro, Gato
	•	Ambas sobrescrevem o método falar():
	•	Cachorro: "Au au!"
	•	Gato: "Miau!"
	•	Crie uma lista com os dois objetos e percorra com um for, chamando falar() para cada.
'''

class Animal:
    def falar(self):
        print("Som genérico")


class Cachorro(Animal):
     def falar(self):
         print("Au Au")

class Gato(Animal):
    def falar(self):
        print("Miau")  

animais = [Animal(), Gato(), Cachorro()]

for i in animais:
    i.falar()

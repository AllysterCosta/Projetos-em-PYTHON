""" Para Iniciar em Programação Orientada a Objetos
Vamos ver agora como implementar uma Classe Pessoa """

class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
        
    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender

""" Será criado agora os objetos Pessoa """

pessoa1 = Pessoa('Maria', 'Rua numero, 123')
pessoa2 = Pessoa('João', 'Rua de numero, 1234')

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')

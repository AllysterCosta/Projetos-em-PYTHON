""" Método de Classe X Método Estático """

from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        #Um método de classe para criar o objeto Pessoa
        #através do ano de Nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
        #Método Estático: verificar se é maior que idade
    @staticmethod
    def eMaiorIdade(idade):
        return idade >= 18
pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)

print('A idade da pessoa 1 é: ', pessoa1.idade)
print('A idade da pessoa 2 é: ', pessoa2.idade)

# Imprimir o resultado
print('A pessoa é maior de idade?', Pessoa.eMaiorIdade(17))



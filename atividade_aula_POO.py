""" Implemente um programa em Python para criar uma classe Veiculo com atributos
"Velocidade Maxima" e "Quilometro percorridos por litro" """

class Veiculo:
    def __init__ (self, nome, velocidade_maxima, quilometros_litro):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.quilometros_litro = quilometros_litro
    
    def capacidade_assentos(self, capacidade):
        print(f'A capacidade de passageiros do veiculo {self.nome} é de {capacidade}')

    def toStr(self):
        print(f'O veiculo é: {self.nome}')
        print(f'Velocidade maxima de {self.velocidade_maxima}')
        print(f'Quilometros por litro percorrido {self.quilometros_litro}')

class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)
    

Onibus1 = Onibus('Mercedes', 190, 12)
Onibus1.toStr()
Onibus1.capacidade_assentos()
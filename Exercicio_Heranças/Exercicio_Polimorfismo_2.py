""" Exemplo de polimorfismo """

class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustível.')
    
class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print('Esse veículo usa Eletricidade')

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()

""" Exemplo de Exceção """

x=10
if x > 5:
    raise Exception('X não pode ser maior que 5. O valor de X é {}'.format(x))
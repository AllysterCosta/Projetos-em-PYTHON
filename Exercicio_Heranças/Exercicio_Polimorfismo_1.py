""" Neste exercicio entederemos Polimorfismo """

class Argentina:
    def capital(self):
        print('Bueno Aires é a capita da Argentina')
    def lingua_oficial(self):
        print('A lingua oficial da Argentina é o Espanhol')

class Brasil:
    def capital(self):
        print('A capital do Brasil é Brasilia')
    def lingua_oficial(self):
        print('Português é a lingua oficial do Brasil.')


obj_arg = Argentina()
obj_bra = Brasil()

for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()
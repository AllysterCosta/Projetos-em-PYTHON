""" Fazendo tratativa de Excessão Personalizada """

class ExcecaoCostumizada(Exception):
    pass

    def throws():
        raise ExcecaoCostumizada()
        try:
            throws()
        except ExcecaoCostumizada as ex:
            print('Excessão Lançada')



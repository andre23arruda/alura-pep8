from fila_base import FilaBase

class Fila_Prioritaria(FilaBase):

    def gera_senha_atual(self)-> None:
        self.senha_atual = f'PR{self.codigo}'

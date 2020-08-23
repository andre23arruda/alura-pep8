from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class Fila_Prioritaria(FilaBase):

    def gera_senha_atual(self)-> None:
        self.senha_atual = f'PR{self.codigo}'

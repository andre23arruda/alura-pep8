from typing import List, Dict, Union

from constantes import TAMANHO_MAXIMO, TAMANHO_MINIMO
from estatistica import EstatisticaDetalhe, EstatisticaResumo

TIPO_ESTATISTICA = Union[EstatisticaResumo, EstatisticaDetalhe]

class FilaBase:
    def __init__(self) -> None:
        self.codigo: int = 0
        self.fila: List[str] = []
        self.clientes_atendidos:List[str] = []
        self.senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO:
            self.codigo = TAMANHO_MINIMO
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'

    def estatistica(self, retorna_estatistica: TIPO_ESTATISTICA) -> dict:
        return retorna_estatistica.get_estatistica(self.clientes_atendidos)
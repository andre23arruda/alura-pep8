from typing import List, Dict, Union

from constantes import TAMANHO_MAXIMO, TAMANHO_MINIMO


class FilaBase:
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos:List[str] = []
    senha_atual: str = ''

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

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        info_estatistica: Dict[str, Union[str, List[str], int]]
        if flag != 'detail':
            info_estatistica[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
        else:
            info_estatistica = {
                'dia': dia,
                'agencia': agencia,
                'clientes_atencidos': self.clientes_atendidos,
                'quantidade_clientes_atendidos': len(self.clientes_atendidos)
            }
        return info_estatistica
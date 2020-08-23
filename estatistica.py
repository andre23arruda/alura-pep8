class EstatisticaResumo:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia
        self.info_estatistica: Dict[str, Union[str, List[str], int]] = {}

    def get_estatistica(self, clientes_atendidos) -> dict:
        self.info_estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)
        return self.info_estatistica


class EstatisticaDetalhe(EstatisticaResumo):
    def get_estatistica(self, clientes_atendidos) -> dict:
        self.info_estatistica = {
            'dia': self.dia,
            'agencia': self.agencia,
            'clientes_atencidos': clientes_atendidos,
            'quantidade_clientes_atendidos': len(clientes_atendidos)
        }
        return self.info_estatistica
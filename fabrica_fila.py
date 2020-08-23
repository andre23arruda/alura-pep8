from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_NORMAL, TIPO_PRIORITARIO


class FabricaFila:
    @staticmethod
    def get_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_PRIORITARIO:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')

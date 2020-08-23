from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica import EstatisticaDetalhe, EstatisticaResumo


fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

fila_teste1 = FilaPrioritaria()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
print(fila_teste1.chama_cliente(5))
print(fila_teste1.chama_cliente(10))
print(fila_teste1.estatistica('12/05/1632', 1, EstatisticaDetalhe))

fila_teste2 = FabricaFila.get_fila('normal')
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(5))
print(fila_teste2.chama_cliente(10))
print(fila_teste2.estatistica('12/05/1632', 1, EstatisticaResumo))
from fila_normal import filanormal
from fila_prioritaria import Fila_Prioritaria

fila_teste = filanormal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(5))
print(fila_teste.chamacliente(10))

fila_teste = Fila_Prioritaria()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))
print(fila_teste.estatistica('12/05/1632', 1, 'detail'))
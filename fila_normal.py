class filanormal:

    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ''

    def gerasenhaatual(self)->None:
        self.senha_atual = f'NM{self.codigo}'

    def resetafila(self)->None:
        if self.codigo >= 100:
            self.codigo = 100
        else:
            self.codigo += 1

    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senha_atual)

    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'

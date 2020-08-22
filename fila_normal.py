class filanormal:

    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ''

    def gerasenhaatual(self)->None:
        self.senha_atual = f'NM{self.codigo}'
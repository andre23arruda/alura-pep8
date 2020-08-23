class FilaBase:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ''

    def reseta_fila(self)-> None:
        if self.codigo >= 100:
            self.codigo = 100
        else:
            self.codigo += 1

    def atualiza_fila(self)-> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int)-> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str)-> dict:
        if flag != 'detail':
            info_estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            info_estatistica = {
                'dia': dia,
                'agencia': agencia,
                'clientes_atencidos': self.clientes_atendidos,
                'num_clientes_atendidos': len(self.clientes_atendidos)
            }
        return info_estatistica

class Processo:
    def __init__(self, id_processo, tempo_chegada, tempo_execucao):
        self.id_processo = id_processo
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.tempo_inicio = None
        self.tempo_fim = None
    
    def __repr__(self):
        # Retorna o id do objeto quando ele for chamado para melhor representar ele na tabela.
        return f"{self.id_processo}"
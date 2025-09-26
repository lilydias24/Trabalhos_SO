
class Processo:
    def __init__(self, id_processo, tempo_chegada, tempo_execucao):
        self.id_processo = id_processo     # Identificador (ex: P1)
        self.tempo_chegada = tempo_chegada      # Arrival Time (AT)
        self.tempo_execucao = tempo_execucao   # Processing Time (PT)
        self.tempo_restante = tempo_execucao   # Tempo restante para execução
        self.tempo_inicio = None           # Primeiro instante de execução
        self.tempo_fim = None             # Instante de término
    
    def __repr__(self):
        # Retorna o id do objeto quando ele for chamado para melhor representar ele na tabela.
        return f"{self.id_processo}(AT={self.tempo_chegada}, PT={self.tempo_execucao}, Rest={self.tempo_restante})"
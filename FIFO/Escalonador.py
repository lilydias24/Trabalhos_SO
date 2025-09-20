class Escalonador:
    def __init__(self):
        self.fila = []
        self.tempo_atual = 0

    def adicionar_processo(self, processo):
        self.fila.append(processo)  
    
    def executar(self):
        while self.fila:
            processo = self.fila.pop(0)
            if processo.tempo_chegada > self.tempo_atual:
                self.tempo_atual = processo.tempo_chegada
            processo.tempo_inicio = self.tempo_atual
            self.tempo_atual += processo.tempo_execucao
            print(f"Processo {processo.id_processo} iniciado em {processo.tempo_inicio} e finalizado em {self.tempo_atual}")
import collections

# Classe que implementa o escalonador FIFO (First In, First Out)
class Escalonador_fifo:
    # Inicializa o escalonador com a lista de processos ordenados pelo tempo de chegada (at).
    def __init__(self, processos):
        self.todos_processos = sorted(processos, key=lambda p: p.tempo_chegada)
        self.processos_disponiveis = collections.deque()
        self.processo_em_execucao = None
        self.tempo_atual = 0
        self.processos_concluidos = []

    # Simula o escalonamento FIFO e imprime uma tabela do estado do sistema a cada unidade de tempo.
    def simular_fifo_com_tabela(self):
        print("--- Simulação FIFO ---")
        print("{:<5} | {:<22} | {:<20} | {:<20} | {:<20}".format(
            "Tempo", "Evento", "Em Execução", "Fila de Prontos", "Tempos Restantes"
        ))
        print("-" * 115)

        # Enquanto houver processos para serem executados a variável evento é criada para registrar o que aconteceu naquele tempo.
        while self.todos_processos or self.processos_disponiveis or self.processo_em_execucao:
            evento = ""

            # 1. Adiciona processos que chegaram no tempo_atual à fila de prontos
            while self.todos_processos and self.todos_processos[0].tempo_chegada <= self.tempo_atual:
                processo = self.todos_processos.pop(0)
                self.processos_disponiveis.append(processo)
                evento += f"Chegada {processo.id_processo} "

            # 2. Se não houver processo em execução, pega um da fila
            if self.processo_em_execucao is None and self.processos_disponiveis:
                self.processo_em_execucao = self.processos_disponiveis.popleft()
                self.processo_em_execucao.tempo_inicio = self.tempo_atual
                evento += f"Início {self.processo_em_execucao.id_processo} "

            # 3. Executa o processo
            if self.processo_em_execucao:
                self.processo_em_execucao.tempo_restante -= 1

                # 4. Verifica se o processo terminou, ou seja, se o tempo restante é zero
                if self.processo_em_execucao.tempo_restante == 0:
                    self.processo_em_execucao.tempo_fim = self.tempo_atual + 1
                    evento += f"Fim {self.processo_em_execucao.id_processo} "
                    self.processos_concluidos.append(self.processo_em_execucao)
                    self.processo_em_execucao = None
            
            # 5. Formata a string de tempos restantes para a tabela
            tempos_restantes_str = ", ".join([f"{p.id_processo}: {p.tempo_restante}" for p in self.processos_disponiveis] + 
                                             ([f"{self.processo_em_execucao.id_processo}: {self.processo_em_execucao.tempo_restante}"] if self.processo_em_execucao else []))

            # Cria a string do processo em execução ou indica que está ocioso
            processo_atual_id = self.processo_em_execucao.id_processo if self.processo_em_execucao else "(Ocioso)"
            
            # Imprime o estado atual do sistema
            print("{:<5} | {:<22} | {:<20} | {:<20} | {:<20}".format(
                self.tempo_atual, evento, processo_atual_id, 
                str(list(self.processos_disponiveis)), tempos_restantes_str
            ))
            
            # Incrementa o tempo atual
            self.tempo_atual += 1

    def executar(self):
        self.simular_fifo_com_tabela()  
        return self.processos_concluidos

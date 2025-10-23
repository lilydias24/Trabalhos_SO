import collections
from T2_SO.cores import colorir, Cores

class Escalonador_fifo:
    def __init__(self, processos):
        self.todos_processos = sorted(processos, key=lambda p: p.tempo_chegada)
        self.processos_disponiveis = collections.deque()
        self.processo_em_execucao = None
        self.tempo_atual = 0
        self.processos_concluidos = []

    def simular_fifo_com_tabela(self):
        print(f"{Cores.VERDE} INICIANDO SIMULAÇÃO FIFO{Cores.RESET}\n")
        
        cabecalho = f"{Cores.NEGRITO}{Cores.CIANO}{'Tempo':<6} | {'Evento':<25} | {'Em Execução':<15} | {'Fila de Prontos':<25} | {'Tempo Restante':<15}{Cores.RESET}"
        separador = f"{Cores.AMARELO}{'-'*100}{Cores.RESET}"
        
        print(cabecalho)
        print(separador)

        while self.todos_processos or self.processos_disponiveis or self.processo_em_execucao:
            evento = ""

            # 1. Adiciona processos que chegaram
            while self.todos_processos and self.todos_processos[0].tempo_chegada <= self.tempo_atual:
                processo = self.todos_processos.pop(0)
                self.processos_disponiveis.append(processo)
                evento += f"{Cores.VERDE}Chegada {processo.id_processo}{Cores.RESET} "

            # 2. Se não houver processo em execução, pega um da fila
            if self.processo_em_execucao is None and self.processos_disponiveis:
                self.processo_em_execucao = self.processos_disponiveis.popleft()
                self.processo_em_execucao.tempo_inicio = self.tempo_atual
                evento += f"{Cores.AZUL}Início {self.processo_em_execucao.id_processo}{Cores.RESET} "

            # 3. Executa o processo
            if self.processo_em_execucao:
                self.processo_em_execucao.tempo_restante -= 1

                # 4. Verifica se o processo terminou
                if self.processo_em_execucao.tempo_restante == 0:
                    self.processo_em_execucao.tempo_fim = self.tempo_atual + 1
                    evento += f"{Cores.VERMELHO}Fim {self.processo_em_execucao.id_processo}{Cores.RESET} "
                    self.processos_concluidos.append(self.processo_em_execucao)
                    self.processo_em_execucao = None
            
            tempos_restantes_str = ", ".join(
                [f"{colorir(p.id_processo, Cores.AMARELO)}:{colorir(str(p.tempo_restante), Cores.AMARELO)}" 
                 for p in self.processos_disponiveis] + 
                ([f"{colorir(self.processo_em_execucao.id_processo, Cores.VERDE)}:{colorir(str(self.processo_em_execucao.tempo_restante), Cores.VERDE)}"] 
                 if self.processo_em_execucao else [])
            )

            processo_atual = colorir(self.processo_em_execucao.id_processo, Cores.VERDE) if self.processo_em_execucao else colorir("(Ocioso)", Cores.CINZA)
            fila_str = ", ".join([colorir(p.id_processo, Cores.AMARELO) for p in self.processos_disponiveis])

            linha = f"{colorir(str(self.tempo_atual), Cores.CIANO):<6} | " \
                    f"{evento:<25} | " \
                    f"{processo_atual:<15} | " \
                    f"[{fila_str}]" + " " * (24 - len(fila_str)) + "| " \
                    f"{tempos_restantes_str}"
            print(linha)
            
            self.tempo_atual += 1

        print(separador)
        print(f"{Cores.VERDE}✅ SIMULAÇÃO FIFO CONCLUÍDA{Cores.RESET}\n")

    def executar(self):
        self.simular_fifo_com_tabela()  
        return self.processos_concluidos
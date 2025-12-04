import random
from typing import List, Dict, Any, Tuple
from collections import deque
from simulador_es.dispositivo import Dispositivo, Teclado, Impressora, Disco
from simulador_es.processo import Processo

class Simulador:
    # O construtor recebe o dicionário de configuração completo
    def __init__(self, configuracao: Dict[str, Any]):
        
        limite_tempo = configuracao.get("limite_tempo_processo", 50)
        taxas = configuracao.get("taxas_interrupcao", {})
        
        # O relógio da simulação
        self.tempo_atual = 0
        # O processo principal que está rodando e será interrompido
        self.processo_principal = Processo(tempo_total_alvo=limite_tempo)
        
        # Lista de todos os dispositivos. A taxa de cada um é passada na inicialização.
        self.dispositivos: List[Dispositivo] = [
            Teclado(taxas.get("Teclado", 0.15)),
            Impressora(taxas.get("Impressora", 0.25)),
            Disco(taxas.get("Disco Rígido", 0.35))
        ]
        
        # Fila de interrupções pendentes. Armazena as interrupções que precisam de tratamento.
        self.fila_interrupcoes = deque()
        # Log de eventos para o relatório final
        self.log_eventos: List[Dict[str, Any]] = []

    def _gerar_interrupcoes(self):
        """
        Verifica se algum dispositivo gerou uma interrupção no ciclo atual.
        """
        for disp in self.dispositivos:
            if disp.gerar_interrupcao():
                # Registra a interrupção na fila.
                self.fila_interrupcoes.append({
                    'tempo': self.tempo_atual,
                    'dispositivo': disp.nome,
                    'prioridade': disp.prioridade
                })

    def _tratar_interrupcao_mais_prioritaria(self):
        """
        Trata a interrupção de maior prioridade na fila.
        """
        if not self.fila_interrupcoes:
            return

        # Ordenar por prioridade as interrupções.
        interrupcoes_ordenadas = sorted(
            list(self.fila_interrupcoes), 
            key=lambda x: x['prioridade'], 
            reverse=True
        )

        # A interrupção a ser tratada é a de maior prioridade.
        interrupcao_ativa = interrupcoes_ordenadas.pop(0)

        # Atualiza a fila de pendentes (removendo a ativa).
        self.fila_interrupcoes = deque(interrupcoes_ordenadas)

        dispositivo_nome = interrupcao_ativa['dispositivo']
        tempo_inicio_tratamento = self.tempo_atual

        # ARMAZENAR CONTEXTO (Salva o PC e muda o estado do Processo Principal para SUSPENSO)
        contexto_salvo = self.processo_principal.salvar_contexto()
        pc_antes = contexto_salvo['pc']
        estado_antes = contexto_salvo['estado_anterior']

        # EXECUTAR TRATAMENTO DA INTERRUPÇÃO (Service Routine)
        # Simula o tempo gasto. 
        tempo_tratamento = random.randint(1, 3) 
        self.tempo_atual += tempo_tratamento # O tempo real avança

        # RESTAURAR CONTEXTO (Restaura o PC e muda o estado do Processo Principal para EXECUTANDO)
        self.processo_principal.restaurar_contexto(contexto_salvo)

        # REGISTRAR LOG
        self.log_eventos.append({
            'tempo_ocorrencia': interrupcao_ativa['tempo'],
            'tempo_inicio_tratamento': tempo_inicio_tratamento,
            'tempo_fim_tratamento': self.tempo_atual,
            'dispositivo': dispositivo_nome,
            'prioridade': interrupcao_ativa['prioridade'],
            'pc_antes': pc_antes,
            'estado_antes': estado_antes,
            'pc_depois': self.processo_principal.tempo_executado,
            'estado_depois': self.processo_principal.estado
        })

    def simular(self):
        """Loop principal da simulação."""
        print(f"--- INICIANDO SIMULAÇÃO (Alvo: {self.processo_principal.tempo_total_alvo} ciclos) ---")

        while not self.processo_principal.executar_ciclo():

            # Geração de Interrupções
            self._gerar_interrupcoes()

            # Tratamento de Interrupções
            # O SO trata a interrupção mais prioritária (e avança o tempo durante o tratamento)
            self._tratar_interrupcao_mais_prioritaria()

            # Avançar o Tempo
            # Se não houve interrupção tratada, o tempo só avança 1 ciclo normal.
            # Se houve tratamento, o tempo já foi avançado dentro de _tratar_interrupcao_mais_prioritaria().
            if not self.fila_interrupcoes:
                 self.tempo_atual += 1


        # Simulação finalizada
        print(f"--- SIMULAÇÃO CONCLUÍDA em T={self.tempo_atual} ---")
        return self.log_eventos
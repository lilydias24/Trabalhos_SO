import random
from typing import List, Dict, Any, Tuple
from collections import deque
from simulador_es.dispositivo import Dispositivo, Teclado, Impressora, Disco
from simulador_es.processo import Processo

class Simulador:
    def __init__(self, limite_tempo: int = 50):
        # O relógio da simulação
        self.tempo_atual = 0
        # O processo principal que está rodando e será interrompido
        self.processo_principal = Processo(tempo_total_alvo=limite_tempo)
        # Lista de todos os dispositivos para geração aleatória de interrupções
        self.dispositivos: List[Dispositivo] = [Teclado(), Impressora(), Disco()]
        
        # Fila de interrupções pendentes. Armazena as interrupções que precisam de tratamento.
        self.fila_interrupcoes = deque()
        # Log de eventos para o relatório final
        self.log_eventos: List[Dict[str, Any]] = []

    def _gerar_interrupcoes(self):
        """
        Verifica se algum dispositivo gerou uma interrupção no ciclo atual.
        (Requisito 1)
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

        # ARMAZENAR CONTEXTO
        contexto_salvo = self.processo_principal.salvar_contexto()
        pc_antes = contexto_salvo['pc']
        estado_antes = contexto_salvo['estado_anterior']
        
        # EXECUTAR TRATAMENTO DA INTERRUPÇÃO
        # Simula o tempo gasto no Service Routine. 
        # O tempo é aleatório para mostrar que o SO está ocupado.
        tempo_tratamento = random.randint(1, 3) 
        self.tempo_atual += tempo_tratamento
        
        # RESTAURAR CONTEXTO
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
            # O SO verifica e trata a interrupção mais prioritária ANTES de o processo principal avançar o tempo no próximo ciclo.
            self._tratar_interrupcao_mais_prioritaria()
            
            # Avançar o Tempo (Avança se não tivermos avançado durante o tratamento)
            # O tempo já é avançado dentro do tratamento de interrupção, mas precisamos avançar 
            # o ciclo principal caso não haja interrupções.
            if self.fila_interrupcoes:
                # Se ainda há interrupções, o tempo já foi avançado dentro do tratamento,
                # então o loop continua e a fila é tratada no próximo ciclo (preempção).
                pass
            else:
                self.tempo_atual += 1
                
        # Simulação finalizada
        print(f"--- SIMULAÇÃO CONCLUÍDA em T={self.tempo_atual} ---")
        return self.log_eventos
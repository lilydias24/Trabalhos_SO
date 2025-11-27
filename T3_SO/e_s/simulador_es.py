import random
import heapq
from typing import List, Dict, Any, Optional, Tuple
from .dispositivo import DispositivoIO, Prioridade
from .processo import ProcessoPrincipal

class EventoLog:
    """Representa um evento para o log."""
    
    def __init__(self, tempo: int, mensagem: str, tipo: str = "INFO"):
        self.tempo = tempo
        self.mensagem = mensagem
        self.tipo = tipo
    
    def __repr__(self):
        return f"[Tempo {self.tempo}] - {self.mensagem}"

class SimuladorGerenciamentoES:
    """Simula o gerenciamento de entrada e saída com interrupções."""
    
    def __init__(self, dispositivos: List[DispositivoIO], tempo_total: int = 100, 
                 probabilidade_interrupcao: float = 0.15):
        """
        Inicializa o simulador de E/S.
        
        Args:
            dispositivos: Lista de dispositivos de E/S disponíveis
            tempo_total: Tempo total de simulação
            probabilidade_interrupcao: Probabilidade de uma interrupção ocorrer a cada unidade de tempo (0.0 a 1.0)
        """
        self.dispositivos = dispositivos
        self.tempo_total = tempo_total
        self.probabilidade_interrupcao = probabilidade_interrupcao
        self.tempo_atual = 0
        self.processo_principal = ProcessoPrincipal()
        self.fila_interrupcoes = []  # Heap para ordenar por prioridade
        self.log_eventos: List[EventoLog] = []
        self.processando_interrupcao = False
        self.tempo_fim_tratamento = -1
        self.interrupcao_atual: Optional[Tuple[DispositivoIO, int]] = None
    
    def adicionar_evento_log(self, mensagem: str, tipo: str = "INFO"):
        """Adiciona um evento ao log."""
        self.log_eventos.append(EventoLog(self.tempo_atual, mensagem, tipo))
    
    def gerar_interrupcao_aleatoria(self) -> Optional[DispositivoIO]:
        """
        Gera uma interrupção aleatória de um dispositivo, se sorteada.
        
        Returns:
            DispositivoIO que gerou a interrupção ou None
        """
        if random.random() < self.probabilidade_interrupcao:
            dispositivo = random.choice(self.dispositivos)
            dispositivo.total_interrupcoes += 1
            return dispositivo
        return None
    
    def adicionar_interrupcao(self, dispositivo: DispositivoIO):
        """Adiciona uma interrupção à fila de prioridades."""
        # Usa heap mínimo, onde prioridade é a chave
        heapq.heappush(self.fila_interrupcoes, (dispositivo.prioridade, self.tempo_atual, dispositivo))
        self.adicionar_evento_log(
            f"Interrupção: {dispositivo.nome} - Prioridade: {dispositivo.obter_info_prioridade()} - Armazenando contexto do processo principal.",
            "INTERRUPCAO"
        )
    
    def obter_proxima_interrupcao(self) -> Optional[DispositivoIO]:
        """Obtém a próxima interrupção da fila (maior prioridade)."""
        if not self.fila_interrupcoes:
            return None
        _, _, dispositivo = heapq.heappop(self.fila_interrupcoes)
        return dispositivo
    
    def processar_interrupcao(self, dispositivo: DispositivoIO):
        """Processa uma interrupção do dispositivo."""
        self.adicionar_evento_log(f"Tratando a interrupção do {dispositivo.nome}.", "TRATAMENTO")
        # O tratamento leva tempo_tratamento unidades de tempo
        self.tempo_fim_tratamento = self.tempo_atual + dispositivo.tempo_tratamento
        self.interrupcao_atual = (dispositivo, self.tempo_atual)
    
    def finalizar_tratamento_interrupcao(self):
        """Finaliza o tratamento da interrupção atual."""
        if self.interrupcao_atual:
            dispositivo, tempo_inicio = self.interrupcao_atual
            self.adicionar_evento_log(
                f"Interrupção tratada ({dispositivo.nome}). Restaurando o contexto do processo principal.",
                "TRATAMENTO"
            )
            self.processo_principal.restaurar_contexto(self.tempo_atual)
            self.adicionar_evento_log("Processo principal retomado.", "RETOMADA")
            self.interrupcao_atual = None
    
    def simular(self) -> List[EventoLog]:
        """
        Executa a simulação completa.
        
        Returns:
            Lista de eventos do log
        """
        # Log inicial
        self.adicionar_evento_log("Processo principal em execução.", "EXECUCAO")
        self.processo_principal.tempo_inicio = 0
        
        while self.tempo_atual < self.tempo_total:
            # Verifica se há tratamento de interrupção em andamento
            if self.processando_interrupcao and self.tempo_atual >= self.tempo_fim_tratamento:
                self.finalizar_tratamento_interrupcao()
                self.processando_interrupcao = False
                self.tempo_fim_tratamento = -1
            
            # Se não está processando interrupção, pode gerar novas e tratar pendentes
            if not self.processando_interrupcao:
                # Tenta gerar nova interrupção
                nova_interrupcao = self.gerar_interrupcao_aleatoria()
                if nova_interrupcao:
                    # Salva contexto apenas se o processo está executando
                    if self.processo_principal.estado == "Executando":
                        contexto = self.processo_principal.salvar_contexto(self.tempo_atual)
                        self.adicionar_evento_log(
                            f"Contexto salvo: {contexto.estado}, PC={contexto.contador_programa}",
                            "CONTEXTO"
                        )
                    self.adicionar_interrupcao(nova_interrupcao)
                
                # Processa próxima interrupção da fila (se houver)
                proxima_interrupcao = self.obter_proxima_interrupcao()
                if proxima_interrupcao:
                    self.processar_interrupcao(proxima_interrupcao)
                    self.processando_interrupcao = True
                else:
                    # Nenhuma interrupção, processo executa normalmente
                    if self.processo_principal.estado == "Executando":
                        self.processo_principal.executar_instrucao()
            
            self.tempo_atual += 1
        
        # Finaliza tratamento pendente, se houver
        if self.processando_interrupcao:
            while self.tempo_atual < self.tempo_fim_tratamento:
                self.tempo_atual += 1
            self.finalizar_tratamento_interrupcao()
        
        return self.log_eventos
    
    def simular_com_multiplas_interrupcoes_simultaneas(self) -> List[EventoLog]:
        """
        Executa a simulação permitindo múltiplas interrupções no mesmo instante.
        
        Returns:
            Lista de eventos do log
        """
        # Log inicial
        self.adicionar_evento_log("Processo principal em execução.", "EXECUCAO")
        self.processo_principal.tempo_inicio = 0
        
        while self.tempo_atual < self.tempo_total:
            # Verifica se há tratamento de interrupção em andamento
            if self.processando_interrupcao and self.tempo_atual >= self.tempo_fim_tratamento:
                self.finalizar_tratamento_interrupcao()
                self.processando_interrupcao = False
                self.tempo_fim_tratamento = -1
            
            # Se não está processando interrupção, pode gerar novas e tratar pendentes
            if not self.processando_interrupcao:
                # Gera todas as interrupções possíveis neste instante
                interrupcoes_instante = []
                for dispositivo in self.dispositivos:
                    if random.random() < self.probabilidade_interrupcao:
                        dispositivo.total_interrupcoes += 1
                        interrupcoes_instante.append(dispositivo)
                
                # Adiciona todas à fila
                if interrupcoes_instante:
                    # Salva contexto apenas uma vez, se o processo está executando
                    if self.processo_principal.estado == "Executando":
                        contexto = self.processo_principal.salvar_contexto(self.tempo_atual)
                        self.adicionar_evento_log(
                            f"Contexto salvo: {contexto.estado}, PC={contexto.contador_programa}",
                            "CONTEXTO"
                        )
                    
                    for dispositivo in interrupcoes_instante:
                        self.adicionar_interrupcao(dispositivo)
                
                # Processa próxima interrupção da fila (se houver)
                proxima_interrupcao = self.obter_proxima_interrupcao()
                if proxima_interrupcao:
                    self.processar_interrupcao(proxima_interrupcao)
                    self.processando_interrupcao = True
                else:
                    # Nenhuma interrupção, processo executa normalmente
                    if self.processo_principal.estado == "Executando":
                        self.processo_principal.executar_instrucao()
            
            self.tempo_atual += 1
        
        # Finaliza tratamento pendente, se houver
        if self.processando_interrupcao:
            while self.tempo_atual < self.tempo_fim_tratamento:
                self.tempo_atual += 1
            self.finalizar_tratamento_interrupcao()
        
        return self.log_eventos
    
    def obter_estatisticas(self) -> Dict[str, Any]:
        """Retorna estatísticas da simulação."""
        total_interrupcoes = sum(d.total_interrupcoes for d in self.dispositivos)
        return {
            "tempo_total": self.tempo_atual,
            "total_interrupcoes": total_interrupcoes,
            "interrupcoes_por_dispositivo": {
                d.nome: d.total_interrupcoes for d in self.dispositivos
            },
            "total_eventos_log": len(self.log_eventos)
        }


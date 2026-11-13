from typing import Dict, Any, Tuple

class Processo:
    """
    Representa o processo principal de execução contínua.
    Seu contexto deve ser salvo e restaurado após uma interrupção.
    """
    
    # Um processo pode estar EXECUTANDO ou SUSPENSO.
    ESTADO_EXECUTANDO = "EXECUTANDO"
    ESTADO_SUSPENSO = "SUSPENSO (Interrompido)"
    
    def __init__(self, pid: int = 1, tempo_total_alvo: int = 100):
        self.pid = pid
        # Simula o Program Counter (PC), ou seja, o ponto de execução atual.
        self.tempo_executado = 0 
        # O estado atual do processo.
        self.estado = self.ESTADO_EXECUTANDO 
        # Objetivo do processo para que ele acabe.
        self.tempo_total_alvo = tempo_total_alvo 

    def salvar_contexto(self) -> Dict[str, Any]:
        """
        Armazena o estado atual (contexto) do processo para retomada posterior.
        O contexto é o valor do tempo_executado.
        """
        contexto = {
            'pc': self.tempo_executado,
            'estado_anterior': self.estado
        }
        self.estado = self.ESTADO_SUSPENSO  # Processo entra em estado suspenso
        return contexto

    def restaurar_contexto(self, contexto: Dict[str, Any]):
        """
        Restaura o estado do processo a partir de um contexto salvo.
        """
        self.tempo_executado = contexto['pc']
        self.estado = self.ESTADO_EXECUTANDO # Processo retorna ao estado de execução

    def executar_ciclo(self):
        """Avança o processo em um ciclo de tempo, se estiver executando."""
        if self.estado == self.ESTADO_EXECUTANDO:
            self.tempo_executado += 1
        
        # Simula a conclusão do processo
        return self.tempo_executado >= self.tempo_total_alvo
from enum import IntEnum
from typing import Dict, Any

class Prioridade(IntEnum):
    """Enumeração das prioridades dos dispositivos."""
    BAIXA = 3
    MEDIA = 2
    ALTA = 1  # Menor número = maior prioridade

class DispositivoIO:
    """Representa um dispositivo de entrada e saída que pode gerar interrupções."""
    
    def __init__(self, nome: str, prioridade: Prioridade, tempo_tratamento: int):
        """
        Inicializa um dispositivo de E/S.
        
        Args:
            nome: Nome do dispositivo (ex: "Teclado", "Impressora", "Disco")
            prioridade: Prioridade do dispositivo (Prioridade.ALTA, MEDIA ou BAIXA)
            tempo_tratamento: Tempo necessário para tratar a interrupção deste dispositivo
        """
        self.nome = nome
        self.prioridade = prioridade
        self.tempo_tratamento = tempo_tratamento
        self.total_interrupcoes = 0
    
    def __lt__(self, other):
        """Permite ordenação por prioridade (menor número = maior prioridade)."""
        return self.prioridade < other.prioridade
    
    def __repr__(self):
        return f"DispositivoIO({self.nome}, Prioridade={self.prioridade.name})"
    
    def obter_info_prioridade(self) -> str:
        """Retorna uma string descritiva da prioridade."""
        prioridade_map = {
            Prioridade.ALTA: "Alta",
            Prioridade.MEDIA: "Média",
            Prioridade.BAIXA: "Baixa"
        }
        return prioridade_map[self.prioridade]


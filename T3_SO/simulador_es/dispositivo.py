import random
from typing import Optional

class Dispositivo:
    """Classe abstrata servindo como base para representar um dispositivo de E/S."""

    # Prioridades: 3 = Alta (atendido primeiro), 1 = Baixa (atendido por último).
    PRIORIDADE_ALTA = 3
    PRIORIDADE_MEDIA = 2
    PRIORIDADE_BAIXA = 1

    def __init__(self, nome: str, prioridade: int, taxa_geracao: float):
        self.nome = nome
        self.prioridade = prioridade
        # Taxa de geração: Chance (0.0 a 1.0) de gerar interrupção por ciclo de tempo.
        self.taxa_geracao = taxa_geracao 

    def __repr__(self):
        return f"{self.nome} (Prio: {self.prioridade})"

    def gerar_interrupcao(self) -> bool:
        """
        Simula a geração de uma interrupção com base na taxa de geração.
        Retorna True se uma interrupção deve ocorrer neste ciclo de tempo.
        """
        # random.random() gera um float entre 0.0 e 1.0. 
        # Se for menor que a taxa_geracao, a interrupção ocorre.
        return random.random() < self.taxa_geracao

# Classes Específicas de Dispositivos
class Teclado(Dispositivo):
    """Dispositivo de alta prioridade (Input Interativo)."""
    def __init__(self, taxa: float):
        super().__init__("Teclado", Dispositivo.PRIORIDADE_ALTA, taxa)

class Impressora(Dispositivo):
    """Dispositivo de média prioridade (Output lento)."""
    def __init__(self, taxa: float):
        super().__init__("Impressora", Dispositivo.PRIORIDADE_MEDIA, taxa)

class Disco(Dispositivo):
    """Dispositivo de baixa prioridade (Transferência de bloco)."""
    def __init__(self, taxa: float):
        super().__init__("Disco Rígido", Dispositivo.PRIORIDADE_BAIXA, taxa)
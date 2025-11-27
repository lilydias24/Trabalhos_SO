from typing import Dict, Any, Optional

class ContextoProcesso:
    """Armazena o contexto de um processo que foi interrompido."""
    
    def __init__(self, tempo_interrupcao: int, estado: str, contador_programa: int, registradores: Dict[str, Any]):
        """
        Inicializa o contexto de um processo.
        
        Args:
            tempo_interrupcao: Tempo em que o processo foi interrompido
            estado: Estado do processo no momento da interrupção
            contador_programa: Valor do contador de programa
            registradores: Dicionário com valores dos registradores
        """
        self.tempo_interrupcao = tempo_interrupcao
        self.estado = estado
        self.contador_programa = contador_programa
        self.registradores = registradores.copy()
    
    def __repr__(self):
        return f"ContextoProcesso(tempo={self.tempo_interrupcao}, estado='{self.estado}', PC={self.contador_programa})"

class ProcessoPrincipal:
    """Representa o processo principal em execução no sistema."""
    
    def __init__(self, nome: str = "Processo Principal"):
        """Inicializa o processo principal."""
        self.nome = nome
        self.contador_programa = 0  # Program Counter
        self.estado = "Executando"
        self.registradores = {
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "DX": 0
        }
        self.contexto_salvo: Optional[ContextoProcesso] = None
        self.tempo_inicio = 0
    
    def salvar_contexto(self, tempo_atual: int) -> ContextoProcesso:
        """
        Salva o contexto atual do processo antes de ser interrompido.
        
        Args:
            tempo_atual: Tempo atual da simulação
            
        Returns:
            ContextoProcesso salvo
        """
        self.contexto_salvo = ContextoProcesso(
            tempo_interrupcao=tempo_atual,
            estado=self.estado,
            contador_programa=self.contador_programa,
            registradores=self.registradores
        )
        self.estado = "Interrompido"
        return self.contexto_salvo
    
    def restaurar_contexto(self, tempo_atual: int):
        """
        Restaura o contexto do processo após o tratamento da interrupção.
        
        Args:
            tempo_atual: Tempo atual da simulação
        """
        if self.contexto_salvo:
            self.contador_programa = self.contexto_salvo.contador_programa
            self.registradores = self.contexto_salvo.registradores.copy()
            self.estado = "Executando"
            self.contexto_salvo = None
    
    def executar_instrucao(self):
        """Simula a execução de uma instrução do processo."""
        self.contador_programa += 1
        # Simula modificações nos registradores
        self.registradores["AX"] = (self.registradores["AX"] + 1) % 1000
        self.registradores["BX"] = (self.registradores["BX"] + 2) % 1000
    
    def obter_estado_formatado(self) -> str:
        """Retorna uma string formatada com o estado atual do processo."""
        return f"Estado: {self.estado}, PC: {self.contador_programa}, AX: {self.registradores['AX']}, BX: {self.registradores['BX']}"


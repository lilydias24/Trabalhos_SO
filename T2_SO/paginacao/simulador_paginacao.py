from collections import deque
from typing import List, Dict, Any, Optional

class PageTableEntry:
    """Representa uma entrada na Tabela de Páginas."""
    def __init__(self):
        self.moldura: Optional[int] = None # Número da moldura física (Frame)
        self.presente: bool = False # Bit de presença: True se estiver na RAM

class SimuladorGerenciadorMemoria:
    """Simula o gerenciamento de memória com paginação e substituição FIFO."""
    def __init__(self, tam_memoria_fisica: int, tam_memoria_virtual: int, tam_pagina: int):
        self.tam_memoria_fisica = tam_memoria_fisica  # em número de molduras (frames)
        self.tam_memoria_virtual = tam_memoria_virtual # em número de páginas
        self.tam_pagina = tam_pagina
        
        # Tabela de Páginas: mapeia o número da página virtual para sua entrada.
        self.tabela_paginas: Dict[int, PageTableEntry] = {
            i: PageTableEntry() for i in range(self.tam_memoria_virtual)
        }
        
        # Memória Física: índice é a moldura, valor é o número da página que a ocupa.
        self.memoria_fisica: List[Optional[int]] = [None] * tam_memoria_fisica 
        
        # Controle FIFO: Fila que armazena o número da página na ordem que entrou na memória.
        self.fila_fifo: deque[int] = deque() 
        
        # Métricas e histórico
        self.total_page_faults = 0
        self.historico_simulacao: List[Dict[str, Any]] = []
        self.tempo_atual = 0

    def traduzir_endereco_virtual(self, endereco_virtual: int) -> int:
        """Calcula o número da página virtual a partir do endereço virtual."""
        # Número da Página Virtual = Endereço Virtual // Tamanho da Página
        num_pagina = endereco_virtual // self.tam_pagina
        
        if num_pagina >= self.tam_memoria_virtual:
            raise ValueError(f"Endereço virtual {endereco_virtual} excede o limite da memória virtual.")
            
        return num_pagina

    def acessar_endereco(self, endereco_virtual: int) -> bool:
        """Simula o acesso a um endereço virtual."""
        
        num_pagina = self.traduzir_endereco_virtual(endereco_virtual)
        entrada_tabela = self.tabela_paginas[num_pagina]
        
        # Evento de simulação
        evento = {
            'tempo': self.tempo_atual,
            'endereco_acessado': endereco_virtual,
            'pagina_alvo': num_pagina,
            'status': '',
            'moldura_encontrada': None,
            'page_fault': False
        }

        # Verifica se página está na memória - BIT DE PRESENÇA (Page Hit)
        if entrada_tabela.presente:
            evento['status'] = 'HIT'
            evento['moldura_encontrada'] = entrada_tabela.moldura
        else:
            # Page Fault - precisa carregar página
            self.total_page_faults += 1
            evento['page_fault'] = True
            evento['status'] = 'FAULT'

            # Encontra moldura livre ou aplica FIFO
            if None in self.memoria_fisica:
                moldura_para_usar = self.memoria_fisica.index(None)
                evento['status'] += ' (Livre)'
            else:
                # FIFO: remove página mais antiga
                pagina_remover = self.fila_fifo.popleft()
                moldura_para_usar = self.memoria_fisica.index(pagina_remover)
                
                # Limpa entrada da página removida
                self.tabela_paginas[pagina_remover].presente = False
                self.tabela_paginas[pagina_remover].moldura = None
                evento['status'] += f' (FIFO Remove P{pagina_remover})'

            # Carrega nova página
            self.memoria_fisica[moldura_para_usar] = num_pagina
            entrada_tabela.moldura = moldura_para_usar
            entrada_tabela.presente = True
            self.fila_fifo.append(num_pagina)
            evento['moldura_encontrada'] = moldura_para_usar

        # Registra evento
        self.historico_simulacao.append(evento)
        self.tempo_atual += 1
        
        return evento['page_fault']

    def simular(self, lista_acessos: List[int]) -> tuple:
        """Executa a simulação completa com a lista de acessos."""
        
        for endereco in lista_acessos:
            try:
                self.acessar_endereco(endereco)
            except ValueError as e:
                print(f"ERRO DE SIMULAÇÃO: {e}")
                break

        return self.historico_simulacao, self.total_page_faults, self.tabela_paginas
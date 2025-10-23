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
        page_fault = False
        
        evento_simulacao = {
            'tempo': self.tempo_atual,
            'endereco_acessado': endereco_virtual,
            'pagina_alvo': num_pagina,
            'status': '',
            'moldura_encontrada': None,
            'page_fault': False,
            'pagina_removida': None
        }

        # 1. VERIFICAÇÃO DO BIT DE PRESENÇA (Page Hit)
        if entrada_tabela.presente:
            # Page Hit
            evento_simulacao['status'] = 'HIT'
            evento_simulacao['moldura_encontrada'] = entrada_tabela.moldura
            
        else:
            # 2. PAGE FAULT (Falta de Página)
            self.total_page_faults += 1
            page_fault = True
            evento_simulacao['page_fault'] = True
            evento_simulacao['status'] = 'FAULT'

            # 3. ENCONTRA UMA MOLDURA LIVRE/PARA SUBSTITUIÇÃO
            if None in self.memoria_fisica:
                # Há espaço livre
                moldura_para_usar = self.memoria_fisica.index(None)
                evento_simulacao['status'] += ' (Livre)'
                
            else:
                # Memória cheia -> Aplicar FIFO
                # Pega a página mais antiga (primeira a entrar)
                pagina_remover = self.fila_fifo.popleft() 
                
                # Encontra a moldura que ela ocupa
                moldura_para_usar = self.memoria_fisica.index(pagina_remover)
                
                # Limpa a entrada na Tabela de Páginas da página removida
                self.tabela_paginas[pagina_remover].presente = False
                
                evento_simulacao['status'] += f' (FIFO Remove P{pagina_remover})'
                evento_simulacao['pagina_removida'] = pagina_remover


            # 4. CARREGAR NOVA PÁGINA (Atualizar Memória Física e Tabela de Páginas)
            
            # Atualiza Memória Física
            self.memoria_fisica[moldura_para_usar] = num_pagina
            
            # Atualiza a Tabela de Páginas da nova página
            entrada_tabela.moldura = moldura_para_usar
            entrada_tabela.presente = True
            
            # Adiciona a nova página ao controle FIFO
            self.fila_fifo.append(num_pagina)
            
            evento_simulacao['moldura_encontrada'] = moldura_para_usar

        # 5. Registrar e Avançar o Tempo
        self.historico_simulacao.append(evento_simulacao)
        self.tempo_atual += 1
        
        return page_fault

    def simular(self, lista_acessos: List[int]) -> tuple:
        """Executa a simulação completa com a lista de acessos."""
        
        for endereco in lista_acessos:
            try:
                self.acessar_endereco(endereco)
            except ValueError as e:
                print(f"ERRO DE SIMULAÇÃO: {e}")
                break

        return self.historico_simulacao, self.total_page_faults, self.tabela_paginas
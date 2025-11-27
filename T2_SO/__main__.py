# main.py

from paginacao.simulador_paginacao import SimuladorGerenciadorMemoria
from cores import Cores, criar_titulo, criar_subtitulo
from utils import exibir_tabela_paginacao_completa
from input_utils import coletar_dados_simulacao # Importação para a nova funcionalidade
import os

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do simulador."""
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE PAGINAÇÃO FIFO", Cores.MAGENTA)
    print(titulo)

def executar_paginacao_fifo():
    
    # 1. Coleta e Validação dos Dados do Usuário
    tam_pagina, tam_memoria_fisica, tam_memoria_virtual, lista_acessos = coletar_dados_simulacao()
    
    # 2. Exibição da Configuração
    print(criar_subtitulo(f"Configuracao: {tam_memoria_fisica} Molduras, Paginas={tam_pagina} Bytes, Algoritmo: FIFO", Cores.AMARELO))

    # 3. Cria e executa simulador
    simulador = SimuladorGerenciadorMemoria(tam_memoria_fisica, tam_memoria_virtual, tam_pagina)
    historico, page_faults_total, tabela_final = simulador.simular(lista_acessos)
    
    # 4. Exibe resultados
    exibir_tabela_paginacao_completa(historico, page_faults_total, tam_memoria_fisica, tabela_final)

def main():
    exibir_cabecalho()
    executar_paginacao_fifo()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
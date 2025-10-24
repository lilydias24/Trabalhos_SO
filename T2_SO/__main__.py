from paginacao.simulador_paginacao import SimuladorGerenciadorMemoria
from cores import Cores, criar_titulo, criar_subtitulo
from utils import exibir_tabela_paginacao_completa
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
    # Configurações que podem ser modificadas
    TAM_PAGINA = 100
    TAM_MEMORIA_FISICA = 3
    TAM_MEMORIA_VIRTUAL = 10
    lista_acessos = [100, 250, 450, 600, 100, 800, 250, 450, 100, 250, 950]
    
    print(criar_subtitulo(f"Configuracao: {TAM_MEMORIA_FISICA} Molduras, Paginas={TAM_PAGINA} Bytes, Algoritmo: FIFO", Cores.AMARELO))

    # Cria e executa simulador
    simulador = SimuladorGerenciadorMemoria(TAM_MEMORIA_FISICA, TAM_MEMORIA_VIRTUAL, TAM_PAGINA)
    historico, page_faults_total, tabela_final = simulador.simular(lista_acessos)
    
    # Exibe resultados, passando todos os dados para a função utilitária
    exibir_tabela_paginacao_completa(historico, page_faults_total, TAM_MEMORIA_FISICA, tabela_final)

def main():
    exibir_cabecalho()
    executar_paginacao_fifo()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
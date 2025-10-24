from paginacao.simulador_paginacao import SimuladorGerenciadorMemoria
from cores import Cores, colorir, criar_titulo, criar_subtitulo
import os

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do simulador."""
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE PAGINAÇÃO FIFO", Cores.MAGENTA)
    print(titulo)

def exibir_tabela_paginacao_completa(historico, page_faults_total, tam_memoria_fisica):
    """Exibe a tabela de simulação passo a passo."""
    
    print("\n" + criar_subtitulo("HISTÓRICO DE ACESSOS E GESTÃO DE MEMÓRIA", Cores.CIANO))
    
    # Calcula largura máxima do status
    largura_status = max(len(estado['status']) for estado in historico) + 3
    largura_status = max(largura_status, 25)  # Mínimo de 25 caracteres
    
    # Cabeçalho com largura ajustada
    print(f"{Cores.NEGRITO}{Cores.AZUL}Tempo | Endereco | Pagina | {'Status':<{largura_status}} | Moldura | Memoria Fisica{Cores.RESET}")
    print(f"{Cores.AMARELO}{'-' * (80 + largura_status - 20)}{Cores.RESET}")
    
    memoria_fisica_atual = [None] * tam_memoria_fisica
    
    # Corpo da Tabela
    for estado in historico:
        pagina_alvo = estado['pagina_alvo']
        status_raw = estado['status']
        moldura_alocada = estado['moldura_encontrada']
        
        # Atualiza memória física
        if moldura_alocada is not None and estado['page_fault']:
            memoria_fisica_atual[moldura_alocada] = pagina_alvo
        
        # Cores baseadas no status
        status_cor = Cores.VERDE if 'HIT' in status_raw else Cores.VERMELHO
        
        # Formata memória física
        frames_str = " | ".join([
            f"P{p}" if p is not None else " - " 
            for p in memoria_fisica_atual
        ])
        
        # Linha com largura ajustada para status
        status_formatado = colorir(status_raw, status_cor)
        print(f"{estado['tempo']:5} | {estado['endereco_acessado']:8} | P{pagina_alvo:4} | {status_formatado:<{largura_status}} | {moldura_alocada:7} | {frames_str}")
        
    print(f"{Cores.AMARELO}{'-' * (80 + largura_status - 20)}{Cores.RESET}")
    
    # Resultado final
    print(f"\n{Cores.MAGENTA}[OK] SIMULAÇÃO CONCLUÍDA{Cores.RESET}")
    print(f"{Cores.MAGENTA}Total de Page Faults: {page_faults_total}{Cores.RESET}\n")

def executar_paginacao_fifo():
    # Configurações
    TAM_PAGINA = 100
    TAM_MEMORIA_FISICA = 3
    TAM_MEMORIA_VIRTUAL = 10
    lista_acessos = [100, 250, 450, 600, 100, 800, 250, 450, 100, 250, 950]
    
    print(criar_subtitulo(f"Configuracao: {TAM_MEMORIA_FISICA} Molduras, Paginas={TAM_PAGINA} Bytes, Algoritmo: FIFO", Cores.AMARELO))

    # Cria e executa simulador
    simulador = SimuladorGerenciadorMemoria(TAM_MEMORIA_FISICA, TAM_MEMORIA_VIRTUAL, TAM_PAGINA)
    historico, page_faults_total, tabela_final = simulador.simular(lista_acessos)
    
    # Exibe resultados
    exibir_tabela_paginacao_completa(historico, page_faults_total, TAM_MEMORIA_FISICA)
    
    # Estado final da tabela de páginas
    print(criar_subtitulo("ESTADO FINAL DA TABELA DE PAGINAS:", Cores.CINZA))
    for p, entry in tabela_final.items():
        if entry.presente:
            print(f"  P{p} -> Moldura {entry.moldura}")
    print()


def main():
    exibir_cabecalho()
    executar_paginacao_fifo()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
from paginacao.simulador_paginacao import SimuladorGerenciadorMemoria
from cores import Cores, colorir, criar_titulo, criar_subtitulo, calcular_comprimento_visivel
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
    """Exibe a tabela de simulação passo a passo com ALINHAMENTO PERFEITO."""
    
    print("\n" + criar_subtitulo("HISTÓRICO DE ACESSOS E GESTÃO DE MEMÓRIA", Cores.CIANO))
    
    # === DEFINIÇÃO DAS LARGURAS VISÍVEIS DAS COLUNAS ===
    LARGURA_TEMPO = 6
    LARGURA_ENDERECO = 10
    LARGURA_PAGINA_ALVO = 10
    LARGURA_STATUS = 28
    LARGURA_MOLDURA = 15
    
    # 1. Cabeçalho (Usamos as larguras para o cabeçalho)
    cabecalho = (
        f"{Cores.NEGRITO}{Cores.AZUL}{'Tempo':<{LARGURA_TEMPO}} | {'Endereço':<{LARGURA_ENDERECO}} | {'Pág. Alvo':<{LARGURA_PAGINA_ALVO}} | "
        f"{'Status':<{LARGURA_STATUS}} | {'Mold. Alocada':<{LARGURA_MOLDURA}} | {'Memória Física (Frames)':<{tam_memoria_fisica*5}}{Cores.RESET}"
    )
    separador = f"{Cores.AMARELO}{'-'*(LARGURA_TEMPO + LARGURA_ENDERECO + LARGURA_PAGINA_ALVO + LARGURA_STATUS + LARGURA_MOLDURA + 15 + tam_memoria_fisica*5)}{Cores.RESET}"
    
    print(cabecalho)
    print(separador)
    
    memoria_fisica_atual = [None] * tam_memoria_fisica
    
    # 2. Corpo da Tabela
    for estado in historico:
        pagina_alvo = estado['pagina_alvo']
        status_raw = estado['status']
        moldura_alocada = estado['moldura_encontrada']
        
        # Atualização e Cores
        if moldura_alocada is not None and estado['page_fault']:
            memoria_fisica_atual[moldura_alocada] = pagina_alvo
        
        status_cor = Cores.BRANCO
        moldura_cor = Cores.BRANCO
        
        if 'HIT' in status_raw:
            status_cor = Cores.VERDE
            moldura_cor = Cores.VERDE
        elif 'FAULT' in status_raw:
            status_cor = Cores.VERMELHO
            moldura_cor = Cores.VERMELHO
            
        # Aplicar cores às strings
        tempo_str = colorir(str(estado['tempo']), Cores.AZUL)
        endereco_str = colorir(str(estado['endereco_acessado']), Cores.AMARELO)
        pagina_alvo_str = colorir(f'P{pagina_alvo}', Cores.BRANCO)
        status_str = colorir(status_raw, status_cor)
        moldura_str = colorir(str(moldura_alocada), moldura_cor)
        
        # Cálculo do Padding para alinhar a tabela
        padding_tempo = " " * (LARGURA_TEMPO - calcular_comprimento_visivel(tempo_str))
        padding_endereco = " " * (LARGURA_ENDERECO - calcular_comprimento_visivel(endereco_str))
        padding_pagina_alvo = " " * (LARGURA_PAGINA_ALVO - calcular_comprimento_visivel(pagina_alvo_str))
        padding_status = " " * (LARGURA_STATUS - calcular_comprimento_visivel(status_str))
        padding_moldura = " " * (LARGURA_MOLDURA - calcular_comprimento_visivel(moldura_str))
        
        # Formata a Memória Física
        frames_str = " | ".join([
            colorir(f"P{p}", Cores.BRANCO) if p is not None else colorir(" - ", Cores.CINZA) 
            for p in memoria_fisica_atual
        ])
        
        # 4. Montagem da Linha (Concatenando string + padding)
        linha = (
            f"{tempo_str}{padding_tempo} | "
            f"{endereco_str}{padding_endereco} | "
            f"{pagina_alvo_str}{padding_pagina_alvo} | "
            f"{status_str}{padding_status} | "
            f"{moldura_str}{padding_moldura} | "
            f"{frames_str}"
        )
        print(linha)
        
    print(separador)
    
    # 3. Resultado Final
    print(f"\n{Cores.MAGENTA}[OK] SIMULACAO CONCLUIDA{Cores.RESET}")
    print(f"{Cores.MAGENTA}Total de Falhas de Pagina (Page Faults): {Cores.NEGRITO}{colorir(page_faults_total, Cores.VERMELHO if page_faults_total > 5 else Cores.VERDE)}{Cores.RESET}\n")

def executar_paginacao_fifo():
    
    # PARÂMETROS DE ENTRADA FIXOS
    TAM_PAGINA = 100
    TAM_MEMORIA_FISICA_FRAMES = 3 # 3 Molduras
    TAM_MEMORIA_VIRTUAL_PAGINAS = 10 
    
    # Lista de acessos a ENDEREÇOS VIRTUAIS
    lista_acessos = [100, 250, 450, 600, 100, 800, 250, 450, 100, 250, 950] 
    
    print(criar_subtitulo(f"Configuracao: {TAM_MEMORIA_FISICA_FRAMES} Molduras (Frames), Paginas={TAM_PAGINA} Bytes. Algoritmo: FIFO.", Cores.AMARELO))

    simulador = SimuladorGerenciadorMemoria(
        tam_memoria_fisica=TAM_MEMORIA_FISICA_FRAMES,
        tam_memoria_virtual=TAM_MEMORIA_VIRTUAL_PAGINAS,
        tam_pagina=TAM_PAGINA
    )
    
    historico, page_faults_total, tabela_final = simulador.simular(lista_acessos)
    
    exibir_tabela_paginacao_completa(historico, page_faults_total, TAM_MEMORIA_FISICA_FRAMES)
    
    # Exibir o estado final da Tabela de Paginas
    print(criar_subtitulo("ESTADO FINAL DA TABELA DE PAGINAS (Resumo):", Cores.CINZA))
    for p, entry in tabela_final.items():
        if entry.presente:
            print(f"  {colorir(f'P{p}', Cores.BRANCO)} -> Moldura {colorir(str(entry.moldura), Cores.AZUL)} (Presente)")
    print()


def main():
    exibir_cabecalho()
    executar_paginacao_fifo()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
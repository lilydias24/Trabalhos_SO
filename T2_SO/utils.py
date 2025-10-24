import re
from cores import Cores, colorir, criar_subtitulo

def calcular_comprimento_visivel(texto_colorido):
    """
    Calcula o comprimento da string ignorando os códigos de cor ANSI.
    """
    texto_sem_cores = re.sub(r'\x1b\[[0-9;]*m', '', texto_colorido)
    return len(texto_sem_cores)

# Constantes para a largura da tabela
LARGURA_TEMPO = 6
LARGURA_ENDERECO = 10
LARGURA_PAGINA_ALVO = 10
LARGURA_MOLDURA = 15

# Função principal de exibição da tabela de paginação
def exibir_tabela_paginacao_completa(historico, page_faults_total, tam_memoria_fisica, tabela_final):
    """
    Exibe a tabela de simulação passo a passo com alinhamento corrigido.
    """
    
    print("\n" + criar_subtitulo("HISTÓRICO DE ACESSOS E GESTÃO DE MEMÓRIA", Cores.CIANO))

    # Determinar a Largura do Status Dinamicamente
    LARGURA_STATUS = max(calcular_comprimento_visivel(estado['status']) for estado in historico) + 1
    LARGURA_STATUS = max(LARGURA_STATUS, 28)
    
    cabecalho = (
        f"{Cores.NEGRITO}{Cores.AZUL}{'Tempo':<{LARGURA_TEMPO}} | {'Endereço':<{LARGURA_ENDERECO}} | {'Pág. Alvo':<{LARGURA_PAGINA_ALVO}} | "
        f"{'Status':<{LARGURA_STATUS}} | {'Mold. Alocada':<{LARGURA_MOLDURA}} | {'Memória Física (Frames)':<{tam_memoria_fisica*5}}{Cores.RESET}"
    )

    separador_len = LARGURA_TEMPO + LARGURA_ENDERECO + LARGURA_PAGINA_ALVO + LARGURA_STATUS + LARGURA_MOLDURA + 15 + tam_memoria_fisica*5
    separador = f"{Cores.AMARELO}{'-'*separador_len}{Cores.RESET}"
    
    print(cabecalho)
    print(separador)
    
    memoria_fisica_atual = [None] * tam_memoria_fisica
    
    # Corpo da Tabela
    for estado in historico:
        pagina_alvo = estado['pagina_alvo']
        status_raw = estado['status']
        moldura_alocada = estado['moldura_encontrada']
        
        # Atualiza memória física
        if moldura_alocada is not None and estado['page_fault']:
            memoria_fisica_atual[moldura_alocada] = pagina_alvo
        
        # Cores
        status_cor = Cores.VERDE if 'HIT' in status_raw else Cores.VERMELHO
        moldura_cor = Cores.VERDE if 'HIT' in status_raw else Cores.VERMELHO

        # Aplicar Cores e Calcular Strings Coloridas
        tempo_str = colorir(str(estado['tempo']), Cores.AZUL)
        endereco_str = colorir(str(estado['endereco_acessado']), Cores.AMARELO)
        pagina_alvo_str = colorir(f'P{pagina_alvo}', Cores.BRANCO)
        status_str = colorir(status_raw, status_cor)
        moldura_str = colorir(str(moldura_alocada), moldura_cor)
        
        # Calcular Padding
        padding_tempo = " " * (LARGURA_TEMPO - calcular_comprimento_visivel(tempo_str))
        padding_endereco = " " * (LARGURA_ENDERECO - calcular_comprimento_visivel(endereco_str))
        padding_pagina_alvo = " " * (LARGURA_PAGINA_ALVO - calcular_comprimento_visivel(pagina_alvo_str))
        padding_status = " " * (LARGURA_STATUS - calcular_comprimento_visivel(status_str))
        padding_moldura = " " * (LARGURA_MOLDURA - calcular_comprimento_visivel(moldura_str))
        
        # Formatar Memória Física
        frames_str = " | ".join([
            colorir(f"P{p}", Cores.BRANCO) if p is not None else colorir(" - ", Cores.CINZA) 
            for p in memoria_fisica_atual
        ])
        
        # Montar cada linha da tabela
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
    
    # Imprime o Resultado Final
    print(f"\n{Cores.MAGENTA}✅ SIMULAÇÃO CONCLUÍDA{Cores.RESET}")
    print(f"{Cores.MAGENTA}Total de Falhas de Página (Page Faults): {colorir(page_faults_total, Cores.VERMELHO if page_faults_total > 5 else Cores.VERDE)}{Cores.RESET}\n")
    
    # Estado final da tabela de páginas
    print(criar_subtitulo("ESTADO FINAL DA TABELA DE PÁGINAS:", Cores.CINZA))
    for p, entry in tabela_final.items():
        if entry.presente:
            print(f"  {colorir(f'P{p}', Cores.BRANCO)} -> Moldura {colorir(str(entry.moldura), Cores.AZUL)}")
    print()
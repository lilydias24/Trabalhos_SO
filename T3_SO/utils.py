import re
from cores import Cores, colorir, criar_subtitulo
from typing import List, Dict, Any, Optional

def calcular_comprimento_visivel(texto_colorido):
    """
    Calcula o comprimento da string ignorando os códigos de cor ANSI.
    """
    texto_sem_cores = re.sub(r'\x1b\[[0-9;]*m', '', texto_colorido)
    return len(texto_sem_cores)

# --- Constantes para a Largura da Tabela de Logs ---
LARGURA_TEMPO_OCORR = 6
LARGURA_DISPOSITIVO = 15
LARGURA_PRIORIDADE = 10
LARGURA_TEMPO_TRATADO = 10
LARGURA_PC_ANTES = 9
LARGURA_PC_DEPOIS = 9
LARGURA_DURACAO_TRAT = 8

def exibir_log_eventos(log_eventos: List[Dict[str, Any]]):
    """
    Exibe o log de interrupções, detalhando o salvamento/restauração do contexto.
    (Requisito 5)
    """
    
    print("\n" + criar_subtitulo("LOG DE TRATAMENTO DE INTERRUPÇÕES", Cores.CIANO))
    # Cores das prioridade
    def cor_prioridade(p):
        if p == 3: return Cores.VERMELHO
        if p == 2: return Cores.AMARELO
        return Cores.VERDE
    
    # --- Cabeçalho ---
    cabecalho = (
        f"{Cores.NEGRITO}{Cores.AZUL}{'Tempo':<{LARGURA_TEMPO_OCORR}} | {'Dispositivo':<{LARGURA_DISPOSITIVO}} | {'Prioridade':<{LARGURA_PRIORIDADE}} | "
        f"{'PC Antes':<{LARGURA_PC_ANTES}} | {'PC Depois':<{LARGURA_PC_DEPOIS}} | {'Duração':<{LARGURA_DURACAO_TRAT}} | {'T. Fim Trat':<{LARGURA_TEMPO_TRATADO}}{Cores.RESET}"
    )

    separador_len = (LARGURA_TEMPO_OCORR + LARGURA_DISPOSITIVO + LARGURA_PRIORIDADE + LARGURA_PC_ANTES + LARGURA_PC_DEPOIS + LARGURA_DURACAO_TRAT + LARGURA_TEMPO_TRATADO + 7 + 10)
    separador = f"{Cores.AMARELO}{'-'*separador_len}{Cores.RESET}"
    
    print(cabecalho)
    print(separador)

    # --- Corpo da Tabela ---
    for evento in log_eventos:
        # PC: Exibe o contexto antes e depois da interrupção
        pc_antes_str = colorir(f"PC={evento['pc_antes']}", Cores.BRANCO)
        pc_depois_str = colorir(f"PC={evento['pc_depois']}", Cores.BRANCO)
        
        # Prioridade
        prioridade_str = colorir(f"{evento['prioridade']} ({evento['dispositivo'][:1]})", cor_prioridade(evento['prioridade']))
        
        # Duração e Tempos
        duracao = evento['tempo_fim_tratamento'] - evento['tempo_inicio_tratamento']
        duracao_str = colorir(str(duracao), Cores.CIANO)
        tempo_ocorrencia_str = colorir(str(evento['tempo_ocorrencia']), Cores.AZUL)
        tempo_fim_str = colorir(str(evento['tempo_fim_tratamento']), Cores.MAGENTA)
        
        # Calcular Padding (Usando as constantes de largura)
        padding_ocorrencia = " " * (LARGURA_TEMPO_OCORR - calcular_comprimento_visivel(tempo_ocorrencia_str))
        padding_dispositivo = " " * (LARGURA_DISPOSITIVO - calcular_comprimento_visivel(evento['dispositivo']))
        padding_prioridade = " " * (LARGURA_PRIORIDADE - calcular_comprimento_visivel(prioridade_str))
        padding_pc_antes = " " * (LARGURA_PC_ANTES - calcular_comprimento_visivel(pc_antes_str))
        padding_pc_depois = " " * (LARGURA_PC_DEPOIS - calcular_comprimento_visivel(pc_depois_str))
        padding_duracao = " " * (LARGURA_DURACAO_TRAT - calcular_comprimento_visivel(duracao_str))
        padding_tempo_fim = " " * (LARGURA_TEMPO_TRATADO - calcular_comprimento_visivel(tempo_fim_str))

        # Montar a Linha
        linha = (
            f"{tempo_ocorrencia_str}{padding_ocorrencia} | "
            f"{evento['dispositivo']}{padding_dispositivo} | "
            f"{prioridade_str}{padding_prioridade} | "
            f"{pc_antes_str}{padding_pc_antes} | "
            f"{pc_depois_str}{padding_pc_depois} | "
            f"{duracao_str}{padding_duracao} | "
            f"{tempo_fim_str}{padding_tempo_fim}"
        )
        print(linha)
        
    print(separador)
    
    # --- Conclusão ---
    print(f"{Cores.MAGENTA}✅ LOG DE INTERRUPÇÕES CONCLUÍDO.{Cores.RESET}")

    print(separador)

def exibir_configuracoes_finais(configuracoes: dict):
    """Exibe os parâmetros de configuração usados na simulação."""
    
    separador_len = (LARGURA_TEMPO_OCORR + LARGURA_DISPOSITIVO + LARGURA_PRIORIDADE + LARGURA_PC_ANTES + LARGURA_PC_DEPOIS + LARGURA_DURACAO_TRAT + LARGURA_TEMPO_TRATADO + 7 + 10)
    separador = f"{Cores.AMARELO}{'-'*separador_len}{Cores.RESET}"
    limite_tempo = configuracoes.get("limite_tempo_processo", 50)
    taxas = configuracoes.get("taxas_interrupcao", {})

    print(criar_subtitulo("PARÂMETROS DA SIMULAÇÃO UTILIZADOS", Cores.MAGENTA))
    
    # Exibe o limite de tempo do processo principal
    print(f" {colorir('-> Limite de Execução do Processo:', Cores.BRANCO)} {colorir(limite_tempo, Cores.CIANO)} ciclos")
    print(f" {colorir('-> Taxas de Geração de Interrupção:', Cores.BRANCO)}")
    
    # Exibe as taxas de interrupção
    for dispositivo, taxa in taxas.items():
        taxa_formatada = f"{taxa * 100:.1f}% ({taxa})"
        print(f"    {colorir(dispositivo, Cores.AMARELO)}: {colorir(taxa_formatada, Cores.VERDE)}")
    
    print(separador)
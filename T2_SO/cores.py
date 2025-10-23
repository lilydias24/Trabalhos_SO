import re

class Cores:
    # Cores básicas
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    SUBLINHADO = '\033[4m'
    
    # Cores do texto
    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'
    CINZA = '\033[90m'  
    
    # Cores de fundo
    FUNDO_PRETO = '\033[40m'
    FUNDO_VERMELHO = '\033[41m'
    FUNDO_VERDE = '\033[42m'
    FUNDO_AMARELO = '\033[43m'
    FUNDO_AZUL = '\033[44m'
    FUNDO_MAGENTA = '\033[45m'
    FUNDO_CIANO = '\033[46m'
    FUNDO_BRANCO = '\033[47m'

def colorir(texto, cor):
    return f"{cor}{texto}{Cores.RESET}"

def criar_titulo(texto, cor=Cores.CIANO):
    linha = "=" * (len(texto) + 4)
    return f"{cor}{linha}\n  {texto}\n{linha}{Cores.RESET}"

def criar_subtitulo(texto, cor=Cores.AMARELO):
    return f"{cor}➤ {texto}{Cores.RESET}"

def calcular_comprimento_visivel(texto_colorido):
    """
    Calcula o comprimento da string ignorando os códigos de cor ANSI.
    """
    texto_sem_cores = re.sub(r'\x1b\[[0-9;]*m', '', texto_colorido)
    return len(texto_sem_cores)
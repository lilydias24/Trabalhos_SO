class Cores:
    # Cores básicas
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    
    # Cores do texto
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'
    CINZA = '\033[90m'

def colorir(texto, cor):
    return f"{cor}{texto}{Cores.RESET}"

def criar_titulo(texto, cor=Cores.CIANO):
    linha = "=" * (len(texto) + 4)
    return f"{cor}{linha}\n  {texto}\n{linha}{Cores.RESET}"

def criar_subtitulo(texto, cor=Cores.AMARELO):
    return f"{cor}-> {texto}{Cores.RESET}"


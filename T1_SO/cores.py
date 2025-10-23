#Configurações de cores para o terminal

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
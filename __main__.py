from fifo.processo import Processo as ProcessoFIFO
from fifo.escalonador_fifo import Escalonador_fifo
from sjf.processo import Processo as ProcessoSJF
from sjf.escalonador_sjf import Escalonador_sjf

# Códigos ANSI para cores
RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CINZA = "\033[90m"

def escolher_escalonador():
    print(f"\n{AZUL}Escolha o algoritmo de escalonamento:{RESET}")
    print(f"{VERDE}1 - FIFO{RESET}")
    print(f"{AMARELO}2 - SJF Preemptivo{RESET}")
    print(f"{VERMELHO}3 - Sair{RESET}")
    escolha = input(f"{CINZA}Digite o número da opção desejada: {RESET}")
    return escolha.strip()


def exibir_tabela(processos):
    print(f"\n{AZUL}{'ID':<5}{'AT':<8}{'PT':<8}{'Início':<10}{'Fim':<8}{'WT':<8}{'TT':<8}{RESET}")
    print("-" * 55)
    for p in processos:
        wt = p.tempo_inicio - p.tempo_chegada
        tt = p.tempo_fim - p.tempo_chegada
        print(f"{VERDE}{p.id_processo:<5}{RESET}{p.tempo_chegada:<8}{p.tempo_execucao:<8}"
              f"{p.tempo_inicio:<10}{p.tempo_fim:<8}{wt:<8}{tt:<8}")
    print("-" * 55)


def main():
    dados_processos = [
        {"id": "P1", "at": 1, "pt": 14},
        {"id": "P2", "at": 5, "pt": 5},
        {"id": "P3", "at": 6, "pt": 12},
        {"id": "P4", "at": 8, "pt": 7},
        {"id": "P5", "at": 13, "pt": 6}
    ]

    while True:
        escolha = escolher_escalonador()
        if escolha == "1":
            processos = [ProcessoFIFO(p['id'], p['at'], p['pt']) for p in dados_processos]
            escalonador = Escalonador_fifo(processos)
            concluidos = escalonador.simular_fifo_com_tabela()
            exibir_tabela(concluidos)
        elif escolha == "2":
            processos = [ProcessoSJF(p['id'], p['at'], p['pt']) for p in dados_processos]
            escalonador = Escalonador_sjf(processos)
            concluidos = escalonador.simular_sjf_com_preempcao_com_tabela()
            exibir_tabela(concluidos)
        elif escolha == "3":
            print(f"{VERMELHO}Finalizando o programa...{RESET}")
            return
        else:
            print(f"{VERMELHO}Opção inválida.{RESET}")


if __name__ == "__main__":
    main()

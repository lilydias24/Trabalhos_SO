from fifo.processo import Processo
from fifo.escalonador_fifo import Escalonador_fifo
from sjf.processo import Processo
from sjf.escalonador_sjf import Escalonador_sjf

def escolher_escalonador():
    print("Escolha o algoritmo de escalonamento:")
    print("1 - FIFO")
    print("2 - SJF Preemptivo")
    print("3 - Sair")
    escolha = input("Digite o número da opção desejada: ")
    return escolha.strip()


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
            processos = [Processo(p['id'], p['at'], p['pt']) for p in dados_processos]
            escalonador = Escalonador_fifo(processos)
            escalonador.simular_fifo_com_tabela()
        elif escolha == "2":
            processos = [Processo(p['id'], p['at'], p['pt']) for p in dados_processos]
            escalonador = Escalonador_sjf(processos)
            escalonador.simular_sjf_com_preempcao_com_tabela()
        elif escolha == "3":
            print("Finalizando o programa...")
            return
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

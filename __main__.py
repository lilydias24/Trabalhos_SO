from fifo.escalonador_fifo import Escalonador_fifo
from sjf.escalonador_sjf import Escalonador_sjf
from metricas import calcular_metricas
from sjf.processo import Processo as ProcessoSJF
from fifo.Processo import Processo as ProcessoFIFO


def exibir_tabela(processos):
    print("\nID   AT      PT      Início    Fim     WT      TT")
    print("------------------------------------------------------------")
    for p in processos:
        tat = p.tempo_fim - p.tempo_chegada           # Turnaround
        wt = tat - p.tempo_execucao                      # Waiting
        inicio = p.tempo_inicio if p.tempo_inicio is not None else "-"
        print(f"{p.id_processo:<5}{p.tempo_chegada:<7}{p.tempo_execucao:<7}{inicio:<9}{p.tempo_fim:<8}{wt:<8}{tat:<8}")


def escolher_escalonador():
    print("\nEscolha o algoritmo de escalonamento:")
    print("1 - FIFO")
    print("2 - SJF (com preempção)")
    opcao = input("Opção: ")
    return opcao


def main():
    opcao = escolher_escalonador()

    if opcao == "1":
        processos = [
            ProcessoFIFO("P1", tempo_chegada=1, tempo_execucao=6),
            ProcessoFIFO("P2", tempo_chegada=5, tempo_execucao=14),
            ProcessoFIFO("P3", tempo_chegada=6, tempo_execucao=5),
            ProcessoFIFO("P4", tempo_chegada=8, tempo_execucao=12),
            ProcessoFIFO("P5", tempo_chegada=13, tempo_execucao=7),
        ]
        escalonador = Escalonador_fifo(processos)
        concluidos = escalonador.executar()

    elif opcao == "2":
        processos = [
            ProcessoSJF("P1", tempo_chegada=1, tempo_execucao=6),
            ProcessoSJF("P2", tempo_chegada=5, tempo_execucao=14),
            ProcessoSJF("P3", tempo_chegada=6, tempo_execucao=5),
            ProcessoSJF("P4", tempo_chegada=8, tempo_execucao=12),
            ProcessoSJF("P5", tempo_chegada=13, tempo_execucao=7),
        ]
        escalonador = Escalonador_sjf(processos)
        concluidos = escalonador.executar()

    else:
        print("Opção inválida.")
        return

    if not concluidos:
        print("Nenhum processo concluído foi retornado pelo escalonador.")
        return

    # Exibe a tabela final dos processos
    exibir_tabela(concluidos)

    # Calcula métricas (TAT, WT, RT e médias)
    calcular_metricas(concluidos)


if __name__ == "__main__":
    main()

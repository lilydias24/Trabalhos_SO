from fifo.escalonador_fifo import Escalonador_fifo
from sjf.escalonador_sjf import Escalonador_sjf
from metricas import calcular_metricas
from sjf.processo import Processo as ProcessoSJF
from fifo.Processo import Processo as ProcessoFIFO
from cores import colorir, criar_titulo, criar_subtitulo, Cores
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE ESCALONAMENTO DE PROCESSOS", Cores.CIANO)
    print(titulo)

def exibir_tabela_processos(processos, algoritmo):
    print(criar_subtitulo(f"RESULTADOS FINAIS - {algoritmo}", Cores.VERDE))
    
    cabecalho = f"{Cores.NEGRITO}{Cores.AZUL}{'ID':<5}{'AT':<6}{'PT':<6}{'Início':<8}{'Fim':<8}{'WT':<8}{'TT':<8}{Cores.RESET}"
    separador = f"{Cores.AMARELO}{'-'*55}{Cores.RESET}"
    
    print(cabecalho)
    print(separador)
    
    for p in processos:
        tat = p.tempo_fim - p.tempo_chegada
        wt = tat - p.tempo_execucao
        inicio = p.tempo_inicio if p.tempo_inicio is not None else "-"
        
        linha = f"{colorir(p.id_processo, Cores.VERDE):<5}" \
                f"\t{colorir(str(p.tempo_chegada), Cores.BRANCO):<6}" \
                f"\t{colorir(str(p.tempo_execucao), Cores.BRANCO):<6}" \
                f"\t{colorir(str(inicio), Cores.AMARELO):<8}" \
                f"\t{colorir(str(p.tempo_fim), Cores.AMARELO):<8}" \
                f"\t{colorir(str(wt), Cores.VERMELHO if wt > 10 else Cores.BRANCO):<8}" \
                f"\t{colorir(str(tat), Cores.CIANO if tat <= 15 else Cores.VERMELHO):<8}"
        print(linha)

def escolher_escalonador():
    print(criar_subtitulo(" ESCOLHA O ALGORITMO DE ESCALONAMENTO", Cores.MAGENTA))
    print(f"\t{Cores.VERDE}1 - FIFO (First In, First Out){Cores.RESET}")
    print(f"\t{Cores.AZUL}2 - SJF Preemptivo (Shortest Job First){Cores.RESET}")
    print(f"\t{Cores.AMARELO}3 - Ambos os algoritmos{Cores.RESET}")
    
    while True:
        opcao = input(f"\n{Cores.CIANO}>>>> Opção (1-3): {Cores.RESET}")
        if opcao in ["1", "2", "3"]:
            return opcao
        print(f"{Cores.VERMELHO}Opção inválida! Escolha 1, 2 ou 3.{Cores.RESET}")

def executar_fifo():
    processos = [
        ProcessoFIFO("P1", tempo_chegada=1, tempo_execucao=6),
        ProcessoFIFO("P2", tempo_chegada=5, tempo_execucao=14),
        ProcessoFIFO("P3", tempo_chegada=6, tempo_execucao=5),
        ProcessoFIFO("P4", tempo_chegada=8, tempo_execucao=12),
        ProcessoFIFO("P5", tempo_chegada=13, tempo_execucao=7),
    ]
    escalonador = Escalonador_fifo(processos)
    return escalonador.executar()

def executar_sjf():
    processos = [
        ProcessoSJF("P1", tempo_chegada=1, tempo_execucao=6),
        ProcessoSJF("P2", tempo_chegada=5, tempo_execucao=14),
        ProcessoSJF("P3", tempo_chegada=6, tempo_execucao=5),
        ProcessoSJF("P4", tempo_chegada=8, tempo_execucao=12),
        ProcessoSJF("P5", tempo_chegada=13, tempo_execucao=7),
    ]
    escalonador = Escalonador_sjf(processos)
    return escalonador.executar()

def main():
    exibir_cabecalho()
    opcao = escolher_escalonador()

    if opcao == "1":
        print(criar_titulo("ALGORITMO FIFO", Cores.VERDE))
        concluidos = executar_fifo()
        exibir_tabela_processos(concluidos, "FIFO")
        calcular_metricas(concluidos)

    elif opcao == "2":
        print(criar_titulo("ALGORITMO SJF PREEMPTIVO", Cores.AZUL))
        concluidos = executar_sjf()
        exibir_tabela_processos(concluidos, "SJF Preemptivo")
        calcular_metricas(concluidos)

    elif opcao == "3":
        print(criar_titulo("COMPARAÇÃO ENTRE ALGORITMOS", Cores.MAGENTA))
        
        print(criar_subtitulo("EXECUTANDO FIFO...", Cores.VERDE))
        concluidos_fifo = executar_fifo()
        exibir_tabela_processos(concluidos_fifo, "FIFO")
        calcular_metricas(concluidos_fifo)
        
        print("\n" + "="*80 + "\n")
        
        print(criar_subtitulo("EXECUTANDO SJF PREEMPTIVO...", Cores.AZUL))
        concluidos_sjf = executar_sjf()
        exibir_tabela_processos(concluidos_sjf, "SJF Preemptivo")
        calcular_metricas(concluidos_sjf)

    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
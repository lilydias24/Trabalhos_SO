from fifo.processo import Processo
from fifo.escalonador_fifo import Escalonador_fifo

def main():
    # Dados do enunciado
    dados_processos = [
        {"id": "P1", "at": 1, "pt": 14},
        {"id": "P2", "at": 5, "pt": 5},
        {"id": "P3", "at": 6, "pt": 12},
        {"id": "P4", "at": 8, "pt": 7},
        {"id": "P5", "at": 13, "pt": 6}
    ]

    # Cria os cinco processos com base nos dados fornecidos
    processos = [Processo(p['id'], p['at'], p['pt']) for p in dados_processos]
    
    escalonador_fifo = Escalonador_fifo(processos)
    escalonador_fifo.simular_fifo_com_tabela()

if __name__ == "__main__":
    main()

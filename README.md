# T1_SO - Trabalho I de Sistemas Operacionais

### Simulação de Gerenciamento de Processos

Projeto desenvolvido como parte do Trabalho Prático I da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa uma simulação de gerenciamento de processos em um sistema operacional, incluindo os algoritmos de escalonamento **FIFO** e **SJF Preemptivo (Shortest Job First)**.

## Integrantes

- Emilly Nascimento Dias – 2410100671
- Eric Santos de Moraes – 2410100672
- Guilherme Rodrigues Vicente – 2410100717

## Estrutura do Projeto

T1_SO/
├── fifo/
│   ├── Processo.py
│   └── escalonador_fifo.py
├── sjf/
│   ├── processo.py
│   └── escalonador_sjf.py
├── cores.py
├── metricas.py
├── __main__.py
└── README.md


## Descrição dos Módulos

- **fifo/**: Implementação do algoritmo FIFO (First In, First Out)
- **sjf/**: Implementação do algoritmo SJF Preemptivo (Shortest Job First)
- **cores.py**: Configurações de cores para exibição no terminal
- **metricas.py**: Cálculo e exibição das métricas de desempenho
- **__main__.py**: Arquivo principal que orquestra a simulação

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
```bash
# navegue até o diretório do projeto
cd T1_SO

# Execute o simulador
python __main__.py

```

# Opções disponíveis:

1 - FIFO (First In, First Out)

2 - SJF Preemptivo (Shortest Job First)

3 - Ambos os algoritmos (para comparação)

A simulação é executada e exibida em formato de tabela em tempo real
Ao final, são apresentadas as métricas de desempenho

# Processos Utilizados
Os processos definidos para a simulação são:

Processo	Tempo de Chegada (AT)	Tempo de Execução (PT)
P1	1	6
P2	5	14
P3	6	5
P4	8	12
P5	13	7

# Algoritmos Implementados
- FIFO (First In, First Out)
Executa os processos na ordem de chegada
Não possui preempção
Simples de implementar, mas pode causar alto tempo de espera para processos curtos que chegam após processos longos
- SJF Preemptivo (Shortest Job First)
Sempre executa o processo com menor tempo de execução restante
Possui preempção: se um processo com tempo menor chega, ele interrompe o processo em execução
Minimiza o tempo médio de espera, mas aumenta o número de trocas de contexto

# Métricas Calculadas
Para cada algoritmo, o sistema calcula:
Waiting Time (WT): Tempo que o processo aguardou na fila de prontos
Turnaround Time (TT): Tempo total desde a chegada até a finalização (TT = WT + PT)
Response Time (RT): Tempo desde a chegada até a primeira execução
Médias: Valores médios de WT, TT e RT para todos os processos

# Exemplo de Saída

Tabela de Execução (exemplo parcial)

Tempo  | Evento                      | Em Execução   | Fila de Prontos        | Tempo Restante
----------------------------------------------------------------------------------------------------
0      |                             | (Ocioso)      | []                     | 
1      | Chegada P1 Início P1        | P1            | []                     | P1:5
...

Tabela de Resultados Finais

ID    AT    PT    Início Fim     WT      TT
-------------------------------------------
P1    1     6     1       7      0       6
P2    5     14    7       21     2       16
...

Métricas

Proc   AT    PT    TAT     WT      RT
-------------------------------------
P1     1     6     6       0       0
P2     5     14    16      2       2
...

MÉDIAS         6.40    2.40    2.40

### Observações

- O projeto foi desenvolvido em Python 3.
- A simulação ocorre em linha de comando.
- O código foi estruturado de forma modular, permitindo futuras expansões para outros algoritmos de escalonamento.
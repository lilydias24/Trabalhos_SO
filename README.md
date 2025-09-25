# T1_SO
Trabalho I de Sistemas Operacionais

### Simulação de Gerenciamento de Processos

Projeto desenvolvido como parte do Trabalho Prático I da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa uma simulação de gerenciamento de processos em um sistema operacional, incluindo os algoritmos de escalonamento FIFO e SJF (Shortest Job First com preempção).

### Integrantes

- Emilly Nascimento Dias – 2410100671
- Eric Santos de Moraes – 2410100672
- Guilherme Rodrigues Vicente – 2410100717

### Estrutura do Projeto
T1_SO/
│── fifo/
│   ├── processo.py
│   └── escalonador_fifo.py
│
│── sjf/
│   ├── processo.py
│   └── escalonador_sjf.py
│
│── __main__.py
│── README.md


- fifo/ → Implementação do algoritmo FIFO.

- sjf/ → Implementação do algoritmo SJF (com e sem preempção).

- main.py → Arquivo principal que executa as simulações e exibe os resultados.

### Como Executar

cd T1_SO

Acesse o repositório e execute o simulador com Python 3:

cd T1_SO
python __main__.py

O programa exibirá os resultados para:

FIFO
SJF Não-Preemptivo
SJF Preemptivo (SRTF)

### Processos Utilizados

Os processos definidos no enunciado foram:

| Processo | Arrival Time (AT) | Processing Time (PT) |
| -------- | ----------------- | -------------------- |
| P1       | 1                 | 14                   |
| P2       | 5                 | 5                    |
| P3       | 6                 | 12                   |
| P4       | 8                 | 7                    |
| P5       | 13                | 6                    |

### Métricas Calculadas

Para cada algoritmo, o sistema calcula:

- Waiting Time (WT) → tempo de espera do processo na fila de prontos.

- Turnaround Time (TT) → tempo total de execução (da chegada até a finalização).

- Médias de WT e TT para comparação entre algoritmos.

### Algoritmos Implementados
-> FIFO (First In, First Out)

- Ordem de execução baseada na chegada dos processos.
- Simples e justo, mas pode causar o efeito comboio, onde processos curtos aguardam longos.

-> SJF (Shortest Job First – Não Preemptivo)

- Seleciona sempre o processo com menor tempo de execução dentre os prontos.
- Uma vez iniciado, o processo executa até o fim.

-> SJF (Shortest Remaining Time First – Preemptivo)

- Seleciona o processo com menor tempo restante.
- Pode interromper um processo em execução se outro com menor tempo chegar.
- Reduz o tempo médio de espera, mas aumenta a quantidade de trocas de contexto.

### Exemplo de Saída

Ao executar o programa, o resultado gerado é semelhante ao seguinte:

=== FIFO ===
P1: WT=0,  TT=14
P2: WT=10, TT=15
P3: WT=23, TT=35
P4: WT=41, TT=48
P5: WT=48, TT=54
Média WT=24.40, Média TT=33.20

=== SJF (Não-Preemptivo) ===
P1: WT=0,  TT=14
P2: WT=9,  TT=14
P3: WT=18, TT=30
P4: WT=22, TT=29
P5: WT=22, TT=28
Média WT=14.20, Média TT=23.00

=== SJF (Preemptivo) ===
P1: WT=7,  TT=21
P2: WT=0,  TT=5
P3: WT=16, TT=28
P4: WT=12, TT=19
P5: WT=9,  TT=15
Média WT=8.80, Média TT=17.60

### Interpretação

FIFO: processos curtos esperam muito tempo (ex.: P2 só inicia após P1).

SJF Não-Preemptivo: melhora as médias, mas processos longos ainda impactam.

SJF Preemptivo (SRTF): garante tempos médios menores, priorizando processos curtos.

### Observações

- O projeto foi desenvolvido em Python 3.
- A simulação ocorre em linha de comando.
- O código foi estruturado de forma modular, permitindo futuras expansões para outros algoritmos de escalonamento.
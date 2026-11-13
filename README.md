# Sistemas Operacionais — simulações em Python

Três simuladores dos mecanismos centrais de um sistema operacional, desenvolvidos nos
trabalhos práticos de Sistemas Operacionais (Engenharia de Software, UNIPAMPA, 2025/2).
Todos rodam no terminal, só com a biblioteca padrão do Python, e mostram o estado do
sistema a cada passo com saída colorida.

| Trabalho | Tema | O que simula |
| --- | --- | --- |
| [T1](T1_SO/) | Gerenciamento de processos | Escalonadores **FIFO** e **SJF preemptivo**, com métricas de tempo de espera |
| [T2](T2_SO/) | Gerenciamento de memória | **Paginação** com substituição de páginas **FIFO**: tradução de endereço virtual para físico, *page hits* e *page faults* |
| [T3](https://github.com/lilydias24/Trabalhos_SO/tree/eric_branch/T3_SO) | Entrada e saída | **Interrupções** de dispositivos tratadas por prioridade, com salvamento e restauração do contexto do processo |

## Como rodar

Python 3, sem dependências. Na pasta de cada trabalho:

```bash
python __main__.py
```

## Minha contribuição

- **T1:** revisão da lógica dos escalonadores FIFO e SJF, métricas de tempo de espera,
  menu principal, saída colorida no terminal e o README.
- **T2:** README do trabalho e uma versão simplificada do simulador de paginação para
  análise (branch `emy_branch`).
- **T3:** revisão do README.

**Equipe:** Emilly Nascimento Dias, Eric Santos de Moraes e Guilherme Rodrigues Vicente.

> O T3 está na branch `eric_branch`; a `main` reúne os trabalhos I e II.

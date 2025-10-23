# T2_SO - Trabalho II de Sistemas Operacionais

### Simulação de Gerenciamento de Memória (Paginação)

Projeto desenvolvido como parte do Trabalho Prático II da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa uma simulação de gerenciamento de memória em um sistema operacional, focando na técnica de Paginação e utilizando o algoritmo de substituição de páginas **FIFO (First-In, First-Out)**.

## Integrantes

- Emilly Nascimento Dias – 2410100671
- Eric Santos de Moraes – 2410100672
- Guilherme Rodrigues Vicente – 2410100717

## Estrutura do Projeto

```
T2_SO/
├── paginacao/
│   └── simulador_paginacao.py
├── cores.py
├── __main__.py
└── README.md
```

## Descrição dos Módulos

- **simulador_paginacao**: Contém a lógica principal da simulação
- **cores.py**: Configurações de cores para exibição no terminal
- **__main__.py**: Arquivo principal que orquestra a simulação

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
```bash
# navegue até o diretório do projeto
cd T2_SO

# Execute o simulador
python __main__.py

```

# Simulação de Paginação

O simulador reproduz o comportamento do Gerenciador de Memória do SO em resposta a uma sequência de acessos a endereços virtuais.

## Configurações Atuais (Constantes Definidas)

| Parâmetro | Descrição | Valor Atual |
| :--- | :--- | :--- |
| **Tamanho da Página** | Tamanho fixo de cada página e moldura. | 100 Bytes |
| **Memória Virtual** | Número total de páginas virtuais. | 10 Páginas |
| **Memória Física** | Número total de molduras (frames) disponíveis na RAM. | 3 Molduras |

## Sequência de Acessos a Endereços Virtuais

A simulação é baseada na seguinte sequência de endereços virtuais, que o código traduz internamente para referências de página (P0, P1, P2, etc.):

```
[100, 250, 450, 600, 100, 800, 250, 450, 100, 250, 950]
```

## Algoritmo Implementado

Substituição de Páginas utilizando FIFO

- Objetivo: Quando ocorre uma Falha de Página e a memória física (RAM) está cheia, a página que está na memória há mais tempo (por ordem de qual chegou primeiro) é a escolhida para ser removida e substituída pela página requisitada.

- Controle: A ordem de entrada é rastreada através de uma fila (deque).

## Saída da Simulação

A simulação exibe um relatório detalhado em formato de tabela, mostrando o estado da memória a cada acesso.

### Métrica Calculada

Total de Falhas de Página (Page Faults): O número total de vezes que a página requisitada não estava na Memória Física.

### Tabela

Ao final, uma tabela é mostrada representando o Estado Final da Tabela de Páginas, mostrando quais páginas virtuais estão mapeadas para qual moldura da RAM.
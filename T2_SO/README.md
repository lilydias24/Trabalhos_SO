# T2_SO - Trabalho II de Sistemas Operacionais

## Simulação de Gerenciamento de Memória (Paginação)

Projeto desenvolvido como parte do Trabalho Prático II da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa uma simulação completa de gerenciamento de memória em um sistema operacional, focando na técnica de **Paginação** e utilizando o algoritmo de substituição de páginas **FIFO (First-In, First-Out)**.

### Objetivo
Demonstrar como funciona o gerenciamento de memória com paginação, incluindo:
- Mapeamento de endereços virtuais para físicos
- Detecção de page hits e page faults
- Substituição de páginas usando algoritmo FIFO
- Visualização do estado da memória em tempo real

## Integrantes

- **Emilly Nascimento Dias** – 2410100671
- **Eric Santos de Moraes** – 2410100672  
- **Guilherme Rodrigues Vicente** – 2410100717

## Estrutura do Projeto

```
T2_SO/
├── paginacao/
│   └── simulador_paginacao.py    # Lógica principal da simulação
├── cores.py                       # Configurações de cores para terminal
├── __main__.py                    # Arquivo principal e interface
├── README.md                      # Documentação do projeto
└── 09_SO_ES_TP2_Simulação do Gerenciamento de Memória.pdf  # Enunciado
```

## Descrição dos Módulos

| Módulo | Descrição | Responsabilidade |
|--------|-----------|------------------|
| **`simulador_paginacao.py`** | Classe principal `SimuladorGerenciadorMemoria` | Implementa o algoritmo FIFO, gerencia tabela de páginas e memória física |
| **`cores.py`** | Utilitários de formatação visual | Fornece cores e formatação para interface do terminal |
| **`__main__.py`** | Interface principal | Orquestra a simulação e exibe resultados formatados |

## Como Executar

### Pré-requisitos
- **Python 3.6+** (recomendado: Python 3.8+)
- **Terminal/Console** com suporte a cores ANSI
- **Sistema Operacional**: Windows, Linux ou macOS

### Execução Rápida
```bash
# 1. Navegue até o diretório do projeto
cd T2_SO

# 2. Execute o simulador
python __main__.py

# 3. Aguarde a simulação completar e pressione Enter para sair
```

### Exemplo de Saída
```
===============================
  SIMULADOR DE PAGINAÇÃO FIFO
===============================

-> Configuração: 3 Molduras (Frames), Páginas=100 Bytes. Algoritmo: FIFO.

-> HISTÓRICO DE ACESSOS E GESTÃO DE MEMÓRIA
Tempo  | Endereço   | Pág. Alvo  | Status                       | Mold. Alocada   | Memória Física (Frames)
---------------------------------------------------------------------------------------------------
0      | 100        | P1         | FAULT (Livre)                | 0               | P1 |  -  |  - 
1      | 250        | P2         | FAULT (Livre)                | 1               | P1 | P2  |  - 
...
```

## Simulação de Paginação

O simulador reproduz o comportamento do Gerenciador de Memória do SO em resposta a uma sequência de acessos a endereços virtuais, demonstrando:

- **Tradução de Endereços**: Conversão de endereços virtuais para números de página
- **Detecção de Page Hits/Faults**: Verificação se a página está na memória física
- **Substituição FIFO**: Remoção da página mais antiga quando necessário
- **Visualização em Tempo Real**: Estado da memória a cada acesso

## Configurações Atuais

| Parâmetro | Descrição | Valor Atual | Impacto |
| :--- | :--- | :--- | :--- |
| **Tamanho da Página** | Tamanho fixo de cada página e moldura | **100 Bytes** | Determina quantos endereços por página |
| **Memória Virtual** | Número total de páginas virtuais | **10 Páginas** | Espaço de endereçamento virtual (0-999) |
| **Memória Física** | Número de molduras (frames) na RAM | **3 Molduras** | Limita páginas simultâneas na memória |

## Sequência de Acessos a Endereços Virtuais

A simulação utiliza a seguinte sequência de endereços virtuais, que são traduzidos internamente para referências de página:

```python
[100, 250, 450, 600, 100, 800, 250, 450, 100, 250, 950]
```

### Tradução de Endereços
| Endereço Virtual | Página | Cálculo |
|------------------|--------|---------|
| 100 | P1 | 100 ÷ 100 = 1 |
| 250 | P2 | 250 ÷ 100 = 2 |
| 450 | P4 | 450 ÷ 100 = 4 |
| 600 | P6 | 600 ÷ 100 = 6 |
| 800 | P8 | 800 ÷ 100 = 8 |
| 950 | P9 | 950 ÷ 100 = 9 |

## Algoritmo FIFO Implementado

### **First-In, First-Out (FIFO)**

**Objetivo**: Quando ocorre uma Falha de Página e a memória física está cheia, a página que está na memória há mais tempo é removida.

**Funcionamento**:
- **Fila de Controle**: Utiliza `deque` para rastrear ordem de entrada
- **Remoção**: `popleft()` remove a página mais antiga
- **Adição**: `append()` adiciona nova página ao final da fila
- **Atualização**: Tabela de páginas e memória física são atualizadas

## Saída da Simulação

A simulação exibe um relatório detalhado em formato de tabela, mostrando o estado da memória a cada acesso.

### Métricas Calculadas

| Métrica | Descrição | Resultado Atual |
|---------|-----------|-----------------|
| **Total de Page Faults** | Número de vezes que a página não estava na memória física | **10/11 acessos (90.9%)** |
| **Page Hits** | Acessos bem-sucedidos a páginas já na memória | **1/11 acessos (9.1%)** |
| **Taxa de Hit** | Percentual de acessos bem-sucedidos | **9.1%** |

### Relatórios Gerados

1. **Tabela de Simulação**: Estado da memória a cada acesso
2. **Estado Final da Tabela de Páginas**: Mapeamento final páginas → molduras
3. **Métricas de Performance**: Contagem de falhas e hits

### Resultados Esperados

Com a configuração atual (3 molduras, 10 páginas virtuais), espera-se:
- **Alto número de page faults** devido à limitação de memória física
- **Comportamento FIFO** correto na substituição de páginas
- **Um page hit** quando acessamos uma página já carregada

## Desenvolvimento

### Tecnologias Utilizadas
- **Python 3.8+** - Linguagem principal
- **Collections.deque** - Estrutura de dados para FIFO
- **ANSI Colors** - Formatação visual no terminal
- **Type Hints** - Documentação de tipos

### Arquitetura
- **Padrão de Classes**: Separação clara de responsabilidades
- **Modularização**: Código organizado em módulos específicos
- **Interface Limpa**: Separação entre lógica e apresentação

### Contribuições dos Integrantes
- **Emilly Nascimento Dias**: Desenvolvimento da lógica principal do simulador e  Interface visual 
- **Eric Santos de Moraes**: Implementação do algoritmo FIFO, testes e documentação 
- **Guilherme Rodrigues Vicente**: Desenvolvimento da lógica principal do simulador e documentação

Este projeto foi desenvolvido para fins educacionais como parte do Trabalho Prático II da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).
## T3_SO - Trabalho III de Sistemas Operacionais

### Simulação de Gerenciamento de E/S (Interrupções)

Projeto desenvolvido como parte do Trabalho Prático III da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa um **Simulador de Gerenciamento de Entrada e Saída**, demonstrando como um Sistema Operacional lida com eventos de hardware assíncronos. O foco principal é a simulação do mecanismo de **Interrupções**, tratamento baseado em **Prioridades** e a rotina de **Salvamento e Restauração de Contexto** (Context Switch).

### Objetivo
Demonstrar o fluxo de execução de um processador sendo interrompido por dispositivos externos, ilustrando:
- Geração aleatória de interrupções por dispositivos (Teclado, Impressora, Disco).
- Tratamento de filas de interrupção baseadas em prioridade.
- O conceito de "Preempção" do processo principal.
- Preservação do *Program Counter* (PC) e estado do processo.

## Integrantes

- **Emilly Nascimento Dias** – 2410100671
- **Eric Santos de Moraes** – 2410100672  
- **Guilherme Rodrigues Vicente** – 2410100717

## Estrutura do Projeto

```

T3_SO/
├── simulador_es/
│   ├── dispositivo.py     # Classes dos dispositivos (Teclado, Disco, etc.) e taxas
│   ├── processo.py        # Representação do processo (PC, Estados, Contexto)
│   └── simulador.py       # Kernel: Loop principal e despachante de interrupções
├── __main__.py            # Ponto de entrada (execução principal)
├── cores.py               # Códigos ANSI para coloração do terminal
├── utils.py               # Funções de formatação de logs e tabelas
├── README.md              # Documentação do projeto
└── .gitignore             # Arquivo de exclusão do Git

````

## Descrição dos Módulos

| Módulo | Responsabilidade |
|--------|------------------|
| **`simulador.py`** | Contém a classe `Simulador`. É o "Kernel" que avança o tempo, verifica a fila de interrupções, decide qual tratar (baseado em prioridade) e orquestra a pausa/retomada do processo. |
| **`processo.py`** | Representa o programa de usuário. Mantém o `tempo_executado` (que simula o Program Counter - PC) e os métodos `salvar_contexto` e `restaurar_contexto`. |
| **`dispositivo.py`** | Define a classe base `Dispositivo` e suas especializações (`Teclado`, `Impressora`, `Disco`). Controla as prioridades e a probabilidade de gerar interrupção. |
| **`utils.py`** | Responsável pela interface visual, gerando a tabela detalhada do Log de Eventos ao final da execução. |

## Como Executar

### Pré-requisitos
- **Python 3.8+** 
- Terminal com suporte a cores ANSI (Linux, macOS, Windows Terminal/PowerShell).

### Passos
1. Navegue até o diretório raiz do projeto:

```bash
   cd T3_SO
````

2.  Execute o arquivo principal:

```bash
    python __main__.py
```

3.  Ao final da execução, o relatório de logs será exibido e você poderá pressionar Enter para sair.

## Configuração da Simulação

Você pode personalizar o comportamento da simulação através do menu quando o programa for executado

## Lógica Implementada

### 1\. Prioridades de Dispositivos

O sistema respeita estritamente a hierarquia de prioridades definida no enunciado:

  * **Alta (3):** Teclado (Dispositivos de caractere/interativos).
  * **Média (2):** Impressora (Output).
  * **Baixa (1):** Disco Rígido (Dispositivos de bloco).

Se múltiplas interrupções ocorrerem no mesmo ciclo, ou se uma nova interrupção chegar enquanto outra aguarda, o `simulador.py` sempre escolherá a de **maior prioridade** para atender primeiro.

### 2\. Mudança de Contexto (Context Switch)

Quando uma interrupção é aceita:

1.  **Salvar:** O simulador chama `processo.salvar_contexto()`. O estado muda de `EXECUTANDO` para `SUSPENSO`, e o valor atual do PC é guardado.
2.  **Tratar:** O SO "gasta" ciclos de CPU (simulados via `random`) para tratar o evento.
3.  **Restaurar:** O simulador chama `processo.restaurar_contexto()`, devolvendo o valor antigo do PC e retornando o estado para `EXECUTANDO`.

### 3\. Exemplo de Saída (Log)

A saída gera uma tabela colorida detalhando o fluxo temporal:

```text
==================================================
  SIMULADOR DE GERENCIAMENTO DE E/S (INTERRUPÇÕES)
==================================================

-> EXECUTANDO PROCESSO PRINCIPAL (Alvo: 50 ciclos)
--- INICIANDO SIMULAÇÃO (Alvo: 50 ciclos) ---
--- SIMULAÇÃO CONCLUÍDA em T=62 ---

-> LOG DE TRATAMENTO DE INTERRUPÇÕES
Tempo  | Dispositivo     | Prioridade | PC Antes  | PC Depois | Duração  | T. Fim Trat
---------------------------------------------------------------------------------------
2      | Disco Rígido    | 1 (D)      | PC=2      | PC=2      | 2        | 4
5      | Teclado         | 3 (T)      | PC=5      | PC=5      | 1        | 6
12     | Impressora      | 2 (I)      | PC=12     | PC=12     | 3        | 15
...
```

  * **Tempo:** Momento em que a interrupção foi gerada.
  * **PC Antes:** Onde o processo estava quando foi interrompido.
  * **PC Depois:** Onde o processo retomou (deve ser igual ao PC Antes).
  * **Duração:** Quanto tempo a CPU ficou ocupada tratando o dispositivo.

```
Este projeto foi desenvolvido para fins educacionais como parte do Trabalho Prático II da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

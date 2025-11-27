# T3_SO - Trabalho III de Sistemas Operacionais

## Simulação de Gerenciamento de Entrada e Saída (E/S)

Projeto desenvolvido como parte do Trabalho Prático III da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).

Este projeto implementa uma simulação completa do gerenciamento de entrada e saída em um sistema operacional, utilizando interrupções para lidar com eventos de hardware, organizando o tratamento por prioridade e garantindo o armazenamento e recuperação do contexto do processo interrompido.

### Objetivo
Demonstrar como funciona o gerenciamento de E/S em um sistema operacional, incluindo:
- Geração de interrupções por dispositivos de hardware
- Tratamento de interrupções por prioridade
- Salvamento e restauração do contexto do processo interrompido
- Registro detalhado de eventos em log

## Integrantes

- **Emilly Nascimento Dias** – 2410100671
- **Eric Santos de Moraes** – 2410100672  
- **Guilherme Rodrigues Vicente** – 2410100717

## Estrutura do Projeto

```
T3_SO/
├── e_s/
│   ├── __init__.py
│   ├── dispositivo.py          # Classes de dispositivos de E/S
│   ├── processo.py             # Classe do processo principal e contexto
│   └── simulador_es.py         # Lógica principal da simulação
├── __main__.py                 # Arquivo principal que orquestra a simulação
├── cores.py                    # Configurações de cores para terminal
├── logger.py                   # Funções para exibição e salvamento de logs
└── README.md                   # Documentação do projeto
```

## Descrição dos Módulos

| Módulo | Descrição | Responsabilidade |
|--------|-----------|------------------|
| **`dispositivo.py`** | Classes `DispositivoIO` e `Prioridade` | Define dispositivos de E/S e suas prioridades |
| **`processo.py`** | Classes `ProcessoPrincipal` e `ContextoProcesso` | Gerencia o processo principal e armazenamento de contexto |
| **`simulador_es.py`** | Classe `SimuladorGerenciamentoES` | Implementa a lógica de simulação de interrupções |
| **`__main__.py`** | Função `main()` e orquestração | Coordena a execução da simulação |
| **`cores.py`** | Utilitários de formatação visual | Fornece cores e formatação para interface do terminal |
| **`logger.py`** | Funções de log | Exibe e salva logs de eventos |

## Como Executar

### Pré-requisitos
- **Python 3.6+** (recomendado: Python 3.8+)
- **Terminal/Console** com suporte a cores ANSI
- **Sistema Operacional**: Windows, Linux ou macOS

### Execução Rápida
```bash
# 1. Navegue até o diretório do projeto
cd T3_SO

# 2. Execute o simulador
python __main__.py

# 3. Escolha o modo de simulação e configure os parâmetros
# 4. Aguarde a simulação completar e pressione Enter para sair
```

### Exemplo de Saída
```
============================================================
  SIMULADOR DE GERENCIAMENTO DE ENTRADA E SAÍDA
============================================================

-> ESCOLHA O MODO DE SIMULAÇÃO
        1 - Simulação com interrupções aleatórias (padrão)
        2 - Simulação com múltiplas interrupções simultâneas

-> PARÂMETROS DA SIMULAÇÃO
Tempo total de simulação (padrão=100): 
Probabilidade de interrupção por unidade de tempo (0.0-1.0, padrão=0.15): 

-> LOG DE EVENTOS
Tempo    Evento
--------------------------------------------------------------------------------
0        Processo principal em execução.
10       Interrupção: Teclado - Prioridade: Alta - Armazenando contexto do processo principal.
10       Contexto salvo: Executando, PC=10
11       Tratando a interrupção do Teclado.
15       Interrupção tratada (Teclado). Restaurando o contexto do processo principal.
16       Processo principal retomado.
...
```

## Funcionalidades

### 1. Dispositivos de E/S

O simulador inclui três dispositivos padrão:

| Dispositivo | Prioridade | Tempo de Tratamento |
|-------------|-----------|---------------------|
| **Teclado** | Alta | 5 unidades de tempo |
| **Impressora** | Média | 8 unidades de tempo |
| **Disco** | Baixa | 10 unidades de tempo |

**Prioridades**: Menor número = maior prioridade (usando heap mínimo)

### 2. Modos de Simulação

#### Modo 1: Interrupções Aleatórias (Padrão)
- Gera uma interrupção aleatória a cada unidade de tempo, baseado na probabilidade configurada
- Trata interrupções uma por vez, respeitando a ordem de prioridade

#### Modo 2: Múltiplas Interrupções Simultâneas
- Permite múltiplas interrupções no mesmo instante
- Testa o mecanismo de prioridade quando várias interrupções chegam ao mesmo tempo
- As interrupções são ordenadas por prioridade e tratadas sequencialmente

### 3. Gerenciamento de Contexto

O sistema implementa:

- **Salvamento de Contexto**: Antes de tratar uma interrupção, o estado atual do processo (registradores, contador de programa, estado) é salvo
- **Restauração de Contexto**: Após tratar a interrupção, o contexto é restaurado e o processo continua sua execução
- **Estado do Processo**: Mantém informações sobre o estado (Executando, Interrompido) e valores dos registradores

### 4. Sistema de Log

O simulador gera um log detalhado contendo:

- **Tempo do evento**: Momento exato em que ocorreu
- **Tipo de evento**: 
  - `EXECUCAO`: Processo principal executando
  - `INTERRUPCAO`: Interrupção detectada
  - `CONTEXTO`: Salvamento/restauração de contexto
  - `TRATAMENTO`: Tratamento da interrupção
  - `RETOMADA`: Retomada do processo principal
- **Dispositivo**: Qual dispositivo gerou a interrupção
- **Prioridade**: Prioridade da interrupção

O log é exibido no terminal e também salvo em um arquivo `log_eventos.txt`.

## Algoritmo de Priorização

O simulador utiliza uma **fila de prioridades** (heap mínimo) para ordenar as interrupções:

1. Interrupções são armazenadas com sua prioridade como chave
2. Menor número de prioridade = maior prioridade (Prioridade.ALTA = 1, MEDIA = 2, BAIXA = 3)
3. O heap garante que a interrupção de maior prioridade seja sempre a próxima a ser tratada
4. Em caso de múltiplas interrupções simultâneas, a ordem de prioridade é respeitada

## Exemplo de Fluxo de Execução

```
[Tempo 0]  - Processo principal em execução.
[Tempo 10] - Interrupção: Teclado - Prioridade: Alta - Armazenando contexto do processo principal.
[Tempo 10] - Contexto salvo: Executando, PC=10
[Tempo 11] - Tratando a interrupção do Teclado.
[Tempo 15] - Interrupção tratada (Teclado). Restaurando o contexto do processo principal.
[Tempo 16] - Processo principal retomado.
[Tempo 20] - Interrupção: Disco - Prioridade: Baixa - Armazenando contexto do processo principal.
[Tempo 20] - Contexto salvo: Executando, PC=16
[Tempo 21] - Tratando a interrupção do Disco.
[Tempo 25] - Interrupção: Impressora - Prioridade: Média - Armazenando contexto do processo principal.
[Tempo 31] - Interrupção tratada (Disco). Restaurando o contexto do processo principal.
[Tempo 32] - Processo principal retomado.
```

## Configurações

### Parâmetros da Simulação

| Parâmetro | Descrição | Valor Padrão | Impacto |
|:--- |:--- |:--- |:--- |
| **Tempo Total** | Duração total da simulação em unidades de tempo | 100 | Determina quanto tempo a simulação roda |
| **Probabilidade de Interrupção** | Probabilidade de gerar interrupção a cada unidade de tempo | 0.15 (15%) | Controla a frequência de interrupções |

### Personalização

Para adicionar novos dispositivos ou modificar os existentes, edite a função `criar_dispositivos_padrao()` no arquivo `__main__.py`:

```python
def criar_dispositivos_padrao() -> list:
    return [
        DispositivoIO("Teclado", Prioridade.ALTA, tempo_tratamento=5),
        DispositivoIO("Impressora", Prioridade.MEDIA, tempo_tratamento=8),
        DispositivoIO("Disco", Prioridade.BAIXA, tempo_tratamento=10),
        DispositivoIO("Mouse", Prioridade.ALTA, tempo_tratamento=3),  # Exemplo
    ]
```

## Estatísticas Geradas

Ao final da simulação, são exibidas:

- **Tempo total de simulação**: Duração total executada
- **Total de interrupções**: Número total de interrupções geradas
- **Interrupções por dispositivo**: Quantidade de interrupções de cada dispositivo
- **Total de eventos no log**: Número de eventos registrados

## Requisitos Atendidos

✅ **Requisito 1**: Simulação de dispositivos de E/S que gerem interrupções aleatoriamente

✅ **Requisito 2**: Cada dispositivo possui prioridade diferente (Teclado=Alta, Impressora=Média, Disco=Baixa)

✅ **Requisito 3**: Identificação, registro e tratamento de interrupções conforme prioridade

✅ **Requisito 4**: Armazenamento e restauração do contexto do processo interrompido

✅ **Requisito 5**: Geração de log detalhado com tempo, dispositivo, prioridade e estado do processo

✅ **Requisito Funcional**: Estruturas de dados para contexto e fila de interrupções

✅ **Requisito Funcional**: Simulação de interrupções simultâneas para testar priorização

## Desenvolvimento

### Tecnologias Utilizadas
- **Python 3.8+** - Linguagem principal
- **heapq** - Estrutura de dados para fila de prioridades
- **enum** - Enumeração de prioridades
- **random** - Geração aleatória de interrupções
- **ANSI Colors** - Formatação visual no terminal

### Arquitetura
- **Padrão de Classes**: Separação clara de responsabilidades
- **Modularização**: Código organizado em módulos específicos
- **Interface Limpa**: Separação entre lógica e apresentação
- **Type Hints**: Documentação de tipos em todas as funções

### Boas Práticas
- Código bem estruturado com funções bem definidas
- Uso de type hints para melhor documentação
- Comentários descritivos em classes e métodos importantes
- Tratamento de erros e validação de entrada
- Logs detalhados para rastreabilidade

## Contribuições dos Integrantes

- **Emilly Nascimento Dias**: Desenvolvimento da lógica principal do simulador e interface visual
- **Eric Santos de Moraes**: Implementação do sistema de prioridades, salvamento de contexto, testes e documentação
- **Guilherme Rodrigues Vicente**: Desenvolvimento da lógica principal do simulador e documentação

## Observações

- O simulador utiliza tempo discreto (unidades de tempo inteiras)
- O tratamento de interrupções é bloqueante (processo principal não executa durante o tratamento)
- Múltiplas interrupções simultâneas são enfileiradas e tratadas por ordem de prioridade
- O log é salvo automaticamente em `log_eventos.txt` no diretório de execução

---

Este projeto foi desenvolvido para fins educacionais como parte do Trabalho Prático III da disciplina de Sistemas Operacionais (UNIPAMPA, 2025/2).


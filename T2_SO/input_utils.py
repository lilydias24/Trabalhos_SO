from typing import List, Tuple
from cores import Cores, colorir

def coletar_inteiro(prompt: str, min_val: int) -> int:
    """Coleta uma entrada de inteiro do usuário com validação."""
    while True:
        try:
            valor = int(input(colorir(prompt, Cores.CIANO)))
            if valor < min_val:
                print(colorir(f"❌ Erro: O valor deve ser no mínimo {min_val}.", Cores.VERMELHO))
            else:
                return valor
        except ValueError:
            print(colorir("❌ Erro: Por favor, insira um número inteiro válido.", Cores.VERMELHO))

def coletar_lista_acessos() -> List[int]:
    """Coleta a lista de acessos virtuais do usuário."""
    while True:
        try:
            entrada = input(colorir("  > Insira a Lista de Acessos Virtuais (separada por vírgulas, ex: 100,250,950): ", Cores.CIANO))
            
            # Remove espaços em branco e divide por vírgula
            acessos_str = [s.strip() for s in entrada.split(',') if s.strip()]
            
            # Converte para lista de inteiros
            lista_acessos = [int(s) for s in acessos_str]
            
            if not lista_acessos:
                 print(colorir("❌ Erro: A lista de acessos não pode estar vazia.", Cores.VERMELHO))
            else:
                return lista_acessos
        except ValueError:
            print(colorir("❌ Erro: Certifique-se de que todos os valores são números inteiros válidos.", Cores.VERMELHO))

def coletar_dados_simulacao() -> Tuple[int, int, int, List[int]]:
    """Coleta e valida todos os parâmetros de entrada do usuário."""
    print(colorir("\n====== CONFIGURAÇÃO DO SIMULADOR ======", Cores.AMARELO))

    tam_pagina = coletar_inteiro("  > Insira o Tamanho da Página (em Bytes, min 1): ", 1)
    tam_memoria_fisica = coletar_inteiro("  > Insira o Número de Molduras (Frames) na Memória Física (min 1): ", 1)
    tam_memoria_virtual = coletar_inteiro("  > Insira o Número Total de Páginas Virtuais (min 1): ", 1)
    
    lista_acessos = coletar_lista_acessos()
    
    # Verifica se os acessos estão dentro da Memória Virtual
    max_endereco_acessado = max(lista_acessos) if lista_acessos else 0
    
    # Endereço mais alto que o processo pode referenciar
    max_limite_mv = (tam_memoria_virtual * tam_pagina) - 1
    
    if max_endereco_acessado > max_limite_mv:
        print(colorir("="*40, Cores.VERMELHO))
        print(colorir("❌ ERRO DE CONFIGURAÇÃO:", Cores.VERMELHO))
        print(colorir(f"O endereço mais alto acessado ({max_endereco_acessado}) excede o limite da Memória Virtual.", Cores.VERMELHO))
        print(colorir(f"Limite Máximo da MV ({tam_memoria_virtual} págs x {tam_pagina} bytes): {max_limite_mv}", Cores.VERMELHO))
        print(colorir("Por favor, aumente o Tamanho da Página ou o Número de Páginas Virtuais.", Cores.VERMELHO))
        print(colorir("="*40, Cores.VERMELHO))
        return coletar_dados_simulacao() # Recomeça o processo
        
    print(colorir("\n✅ Configurações validadas com sucesso!", Cores.VERDE))
    return tam_pagina, tam_memoria_fisica, tam_memoria_virtual, lista_acessos
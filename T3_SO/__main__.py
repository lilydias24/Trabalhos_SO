from simulador_es.simulador import Simulador
from cores import Cores, criar_titulo, criar_subtitulo, colorir
from utils import exibir_configuracoes_finais, exibir_log_eventos
from typing import Dict, Any
import os

# Configuração padrão do programa
DEFAULT_CONFIG = {
    "limite_tempo_processo": 50,
    "taxas_interrupcao": {
        "Teclado": 0.15,
        "Impressora": 0.25,
        "Disco Rígido": 0.35
    }
}

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do simulador."""
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE GERENCIAMENTO DE E/S (INTERRUPÇÕES)", Cores.CIANO)
    print(titulo)

def ler_entrada_int(prompt: str, min_val: int = 1) -> int:
    """Função auxiliar para ler entradas inteiras com validação."""
    while True:
        try:
            valor = input(colorir(prompt, Cores.BRANCO))
            numero = int(valor)
            if numero >= min_val:
                return numero
            print(colorir(f"Valor inválido. Digite um número inteiro maior ou igual a {min_val}.", Cores.VERMELHO))
        except ValueError:
            print(colorir("Entrada inválida. Digite um número inteiro.", Cores.VERMELHO))

def ler_entrada_percentual(prompt: str) -> float:
    """Função auxiliar para ler entradas de porcentagem (0-100) e converter para taxa (0.0-1.0)."""
    while True:
        try:
            valor = input(colorir(prompt, Cores.BRANCO))
            porcentagem = int(valor)
            if 0 <= porcentagem <= 100:
                return porcentagem / 100.0
            print(colorir("Porcentagem inválida. Digite um valor entre 0 e 100.", Cores.VERMELHO))
        except ValueError:
            print(colorir("Entrada inválida. Digite um número inteiro (0-100).", Cores.VERMELHO))


def coletar_configuracao_cli() -> Dict[str, Any]:
    """Coleta as configurações do usuário via linha de comando."""
    
    config = DEFAULT_CONFIG.copy()
    
    print(criar_subtitulo("CONFIGURAÇÃO DA SIMULAÇÃO", Cores.AMARELO))
    
    # 1. Escolha de configurações padrão
    print(f"\n{colorir('Deseja usar as configurações padrão?', Cores.CIANO)}")
    print(f"{Cores.VERDE}  Padrão:{Cores.RESET} Limite de Tempo = {DEFAULT_CONFIG['limite_tempo_processo']} ciclos")
    print(f"{Cores.VERDE}  Padrão:{Cores.RESET} Taxas de Interrupção (Teclado: {DEFAULT_CONFIG['taxas_interrupcao']['Teclado']*100:.0f}%, Impressora: {DEFAULT_CONFIG['taxas_interrupcao']['Impressora']*100:.0f}%, Disco: {DEFAULT_CONFIG['taxas_interrupcao']['Disco Rígido']*100:.0f}%)")
    
    escolha = input(colorir("  [S] (Padrão) / [N] (Personalizar): ", Cores.BRANCO)).strip().lower()

    if escolha != 'n':
        print(colorir("\n Usando configurações padrão.", Cores.VERDE))
        return config

    print(colorir("\n Personalizando configurações...", Cores.MAGENTA))
    
    # 2. Configurações personalizadas
    
    # 2.1 Limite de Tempo do Processo
    print(criar_subtitulo("Limite de Tempo do Processo Principal", Cores.AMARELO))
    limite = ler_entrada_int("  Digite o limite de tempo (ciclos) para o processo: ", min_val=5)
    config["limite_tempo_processo"] = limite
    
    # 2.2 Taxas de Interrupção
    print(criar_subtitulo("\nTaxas de Geração de Interrupção (em %)", Cores.AMARELO))
    
    for dispositivo in config["taxas_interrupcao"].keys():
        taxa_padrao = config["taxas_interrupcao"][dispositivo]
        prompt = f"  Taxa do {dispositivo} (Padrão: {taxa_padrao*100:.0f}%): "
        nova_taxa = ler_entrada_percentual(prompt)
        config["taxas_interrupcao"][dispositivo] = nova_taxa

    return config

def executar_simulacao_es():

    # 1. Coleta a configuração via CLI
    configuracao = coletar_configuracao_cli()
    
    # Obtém o limite de tempo para a mensagem de início
    LIMITE_TEMPO_PROCESSO = configuracao.get("limite_tempo_processo", 50)

    print(criar_subtitulo(f"\nEXECUTANDO PROCESSO PRINCIPAL (Alvo: {LIMITE_TEMPO_PROCESSO} ciclos)", Cores.AMARELO))

    # 2. Cria e executa o simulador com a nova configuração
    simulador = Simulador(configuracao=configuracao)
    log_eventos = simulador.simular()

    # 3. Exibe os resultados (Log de Eventos)
    if log_eventos:
        exibir_log_eventos(log_eventos)
    else:
        print(f"{Cores.VERDE}Nenhuma interrupção ocorreu durante a execução.{Cores.RESET}")

    # 4. Exibe as configurações utilizadas, passando o dicionário completo
    exibir_configuracoes_finais(configuracao)

def main():
    exibir_cabecalho()
    executar_simulacao_es()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
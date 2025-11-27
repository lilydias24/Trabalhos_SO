import os
from e_s.simulador_es import SimuladorGerenciamentoES
from e_s.dispositivo import DispositivoIO, Prioridade
from cores import Cores, criar_titulo, criar_subtitulo, colorir
from logger import exibir_log_eventos, salvar_log_arquivo, exibir_estatisticas

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do simulador."""
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE GERENCIAMENTO DE ENTRADA E SAÍDA", Cores.CIANO)
    print(titulo)

def criar_dispositivos_padrao() -> list:
    """Cria os dispositivos padrão do sistema."""
    return [
        DispositivoIO("Teclado", Prioridade.ALTA, tempo_tratamento=5),
        DispositivoIO("Impressora", Prioridade.MEDIA, tempo_tratamento=8),
        DispositivoIO("Disco", Prioridade.BAIXA, tempo_tratamento=10)
    ]

def escolher_modo_simulacao():
    """Permite ao usuário escolher o modo de simulação."""
    print(criar_subtitulo(" ESCOLHA O MODO DE SIMULAÇÃO", Cores.MAGENTA))
    print(f"\t{Cores.VERDE}1 - Simulação com interrupções aleatórias (padrão){Cores.RESET}")
    print(f"\t{Cores.AZUL}2 - Simulação com múltiplas interrupções simultâneas{Cores.RESET}")
    
    while True:
        opcao = input(f"\n{Cores.CIANO}>>>> Opção (1-2, padrão=1): {Cores.RESET}").strip()
        if opcao == "" or opcao == "1":
            return 1
        elif opcao == "2":
            return 2
        print(f"{Cores.VERMELHO}Opção inválida! Escolha 1 ou 2.{Cores.RESET}")

def obter_parametros_simulacao():
    """Obtém os parâmetros da simulação do usuário."""
    print(criar_subtitulo(" PARÂMETROS DA SIMULAÇÃO", Cores.AMARELO))
    
    # Tempo total
    while True:
        try:
            tempo_input = input(f"{Cores.BRANCO}Tempo total de simulação (padrão=100): {Cores.RESET}").strip()
            tempo_total = int(tempo_input) if tempo_input else 100
            if tempo_total > 0:
                break
            print(f"{Cores.VERMELHO}O tempo deve ser maior que 0.{Cores.RESET}")
        except ValueError:
            print(f"{Cores.VERMELHO}Por favor, insira um número válido.{Cores.RESET}")
    
    # Probabilidade de interrupção
    while True:
        try:
            prob_input = input(f"{Cores.BRANCO}Probabilidade de interrupção por unidade de tempo (0.0-1.0, padrão=0.15): {Cores.RESET}").strip()
            probabilidade = float(prob_input) if prob_input else 0.15
            if 0.0 <= probabilidade <= 1.0:
                break
            print(f"{Cores.VERMELHO}A probabilidade deve estar entre 0.0 e 1.0.{Cores.RESET}")
        except ValueError:
            print(f"{Cores.VERMELHO}Por favor, insira um número válido.{Cores.RESET}")
    
    return tempo_total, probabilidade

def executar_simulacao(modo: int, tempo_total: int, probabilidade: float):
    """Executa a simulação de gerenciamento de E/S."""
    dispositivos = criar_dispositivos_padrao()
    
    print(criar_subtitulo(" CONFIGURAÇÃO", Cores.AMARELO))
    print(f"{Cores.BRANCO}Dispositivos configurados:{Cores.RESET}")
    for dispositivo in dispositivos:
        print(f"  {Cores.CIANO}• {dispositivo.nome}{Cores.RESET} - Prioridade: {colorir(dispositivo.obter_info_prioridade(), Cores.VERDE)}, "
              f"Tempo de tratamento: {dispositivo.tempo_tratamento}")
    print(f"{Cores.BRANCO}Tempo total: {colorir(str(tempo_total), Cores.CIANO)}{Cores.RESET}")
    print(f"{Cores.BRANCO}Probabilidade de interrupção: {colorir(str(probabilidade), Cores.CIANO)}{Cores.RESET}\n")
    
    simulador = SimuladorGerenciamentoES(
        dispositivos=dispositivos,
        tempo_total=tempo_total,
        probabilidade_interrupcao=probabilidade
    )
    
    # Executa simulação de acordo com o modo
    if modo == 1:
        log_eventos = simulador.simular()
    else:
        log_eventos = simulador.simular_com_multiplas_interrupcoes_simultaneas()
    
    # Exibe resultados
    exibir_log_eventos(log_eventos)
    exibir_estatisticas(simulador.obter_estatisticas())
    
    # Salva log em arquivo
    salvar_log_arquivo(log_eventos)
    
    return log_eventos

def main():
    """Função principal do programa."""
    exibir_cabecalho()
    
    modo = escolher_modo_simulacao()
    tempo_total, probabilidade = obter_parametros_simulacao()
    
    print()  # Linha em branco
    executar_simulacao(modo, tempo_total, probabilidade)
    
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()


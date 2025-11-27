from simulador_es.simulador import Simulador
from cores import Cores, criar_titulo, criar_subtitulo
from utils import exibir_configuracoes_finais, exibir_log_eventos
from gerenciador_configuracao import CONFIG
import os

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do simulador."""
    limpar_tela()
    titulo = criar_titulo("SIMULADOR DE GERENCIAMENTO DE E/S (INTERRUPÇÕES)", Cores.CIANO)
    print(titulo)

def executar_simulacao_es():
    
    # Lê o limite de tempo do arquivo de configuração
    LIMITE_TEMPO_PROCESSO = CONFIG.get("limite_tempo_processo", 50)
    
    print(criar_subtitulo(f"EXECUTANDO PROCESSO PRINCIPAL (Alvo: {LIMITE_TEMPO_PROCESSO} ciclos)", Cores.AMARELO))

    # Cria e executa o simulador
    simulador = Simulador(limite_tempo=LIMITE_TEMPO_PROCESSO)
    log_eventos = simulador.simular()
    
    # Exibe os resultados (Log de Eventos)
    if log_eventos:
        exibir_log_eventos(log_eventos)
    else:
        print(f"{Cores.VERDE}Nenhuma interrupção ocorreu durante a execução.{Cores.RESET}")
    
    # Exibe as configurações utilizadas, passando o dicionário CONFIG
    exibir_configuracoes_finais(CONFIG)

def main():
    exibir_cabecalho()
    executar_simulacao_es()
    input(f"\n{Cores.CIANO}Pressione Enter para sair...{Cores.RESET}")

if __name__ == "__main__":
    main()
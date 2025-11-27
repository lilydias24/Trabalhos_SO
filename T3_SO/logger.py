from typing import List
from e_s.simulador_es import EventoLog
from cores import Cores, colorir, criar_titulo, criar_subtitulo

def exibir_log_eventos(eventos: List[EventoLog]):
    """Exibe os eventos do log formatados no terminal."""
    print("\n" + criar_subtitulo("LOG DE EVENTOS", Cores.CIANO))
    print(f"{Cores.NEGRITO}{'Tempo':<8} {'Evento'}{Cores.RESET}")
    print("-" * 80)
    
    for evento in eventos:
        cor_evento = Cores.BRANCO
        if evento.tipo == "INTERRUPCAO":
            cor_evento = Cores.VERMELHO
        elif evento.tipo == "TRATAMENTO":
            cor_evento = Cores.AMARELO
        elif evento.tipo == "RETOMADA":
            cor_evento = Cores.VERDE
        elif evento.tipo == "EXECUCAO":
            cor_evento = Cores.AZUL
        elif evento.tipo == "CONTEXTO":
            cor_evento = Cores.MAGENTA
        
        tempo_str = colorir(f"{evento.tempo}", Cores.CIANO)
        mensagem_str = colorir(evento.mensagem, cor_evento)
        print(f"{tempo_str:<8} {mensagem_str}")

def salvar_log_arquivo(eventos: List[EventoLog], nome_arquivo: str = "log_eventos.txt"):
    """
    Salva o log de eventos em um arquivo de texto.
    
    Args:
        eventos: Lista de eventos do log
        nome_arquivo: Nome do arquivo onde salvar o log
    """
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("=" * 80 + "\n")
            arquivo.write("LOG DE EVENTOS - SIMULAÇÃO DE GERENCIAMENTO DE E/S\n")
            arquivo.write("=" * 80 + "\n\n")
            
            for evento in eventos:
                arquivo.write(f"[Tempo {evento.tempo}] - {evento.mensagem}\n")
            
            arquivo.write("\n" + "=" * 80 + "\n")
        
        print(f"\n{Cores.VERDE}✓ Log salvo em: {nome_arquivo}{Cores.RESET}")
    except Exception as e:
        print(f"{Cores.VERMELHO}Erro ao salvar log: {e}{Cores.RESET}")

def exibir_estatisticas(estatisticas: dict):
    """Exibe as estatísticas da simulação."""
    print("\n" + criar_subtitulo("ESTATÍSTICAS DA SIMULAÇÃO", Cores.VERDE))
    print(f"{Cores.BRANCO}Tempo total de simulação: {colorir(str(estatisticas['tempo_total']), Cores.CIANO)}{Cores.RESET}")
    print(f"{Cores.BRANCO}Total de interrupções: {colorir(str(estatisticas['total_interrupcoes']), Cores.VERMELHO)}{Cores.RESET}")
    print(f"{Cores.BRANCO}Total de eventos no log: {colorir(str(estatisticas['total_eventos_log']), Cores.AMARELO)}{Cores.RESET}")
    
    print(f"\n{Cores.NEGRITO}Interrupções por dispositivo:{Cores.RESET}")
    for dispositivo, quantidade in estatisticas['interrupcoes_por_dispositivo'].items():
        print(f"  {colorir(dispositivo, Cores.CIANO)}: {colorir(str(quantidade), Cores.AMARELO)}")


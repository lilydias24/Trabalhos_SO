from cores import colorir, criar_titulo, Cores

def calcular_metricas(processos):
    soma_tat = soma_wt = soma_rt = 0
    n = len(processos)

    print(f"\n{Cores.VERDE} MÉTRICAS DOS PROCESSOS{Cores.RESET}")
    separador = f"{Cores.AMARELO}{'-'*55}{Cores.RESET}"
    cabecalho = f"{Cores.NEGRITO}{Cores.CIANO}{'Proc':<6}{'AT':<6}{'PT':<6}{'TAT':<8}{'WT':<8}{'RT':<8}{Cores.RESET}"
    
    print(separador)
    print(cabecalho)
    print(separador)

    for p in processos:
        tat = p.tempo_fim - p.tempo_chegada
        wt = tat - p.tempo_execucao
        rt = (p.tempo_inicio - p.tempo_chegada) if p.tempo_inicio is not None else 0

        soma_tat += tat
        soma_wt += wt
        soma_rt += rt

        # Cores baseadas nos valores
        cor_wt = Cores.VERMELHO if wt > 10 else (Cores.AMARELO if wt > 5 else Cores.VERDE)
        cor_tat = Cores.VERMELHO if tat > 20 else (Cores.AMARELO if tat > 10 else Cores.VERDE)
        cor_rt = Cores.VERMELHO if rt > 10 else (Cores.AMARELO if rt > 5 else Cores.VERDE)

        linha = f"{colorir(p.id_processo, Cores.VERDE):<6}" \
                f"\t{colorir(str(p.tempo_chegada), Cores.BRANCO):<6}" \
                f"\t{colorir(str(p.tempo_execucao), Cores.BRANCO):<6}" \
                f"\t{colorir(str(tat), cor_tat):<8}" \
                f"\t{colorir(str(wt), cor_wt):<8}" \
                f"\t{colorir(str(rt), cor_rt):<8}"
        print(linha)

    print(separador)
    
    # Médias com cores
    media_tat = soma_tat / n
    media_wt = soma_wt / n
    media_rt = soma_rt / n
    
    cor_media_tat = Cores.VERMELHO if media_tat > 20 else (Cores.AMARELO if media_tat > 10 else Cores.VERDE)
    cor_media_wt = Cores.VERMELHO if media_wt > 10 else (Cores.AMARELO if media_wt > 5 else Cores.VERDE)
    
    print(f"{Cores.NEGRITO}{'MÉDIAS':<12} {colorir(f'{media_tat:.2f}', cor_media_tat):<10} {colorir(f'{media_wt:.2f}', cor_media_wt):<10} {colorir(f'{media_rt:.2f}', Cores.CIANO):<10}{Cores.RESET}")
    
    # Interpretação das médias
    print(f"\n{Cores.CIANO} INTERPRETAÇÃO:{Cores.RESET}")
    if media_wt < 5:
        print(f"{Cores.VERDE}✓ Excelente tempo de espera médio{Cores.RESET}")
    elif media_wt < 10:
        print(f"{Cores.AMARELO}● Tempo de espera médio aceitável{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}⚠ Tempo de espera médio elevado{Cores.RESET}")
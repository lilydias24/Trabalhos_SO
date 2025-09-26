def calcular_metricas(processos):
    soma_tat = soma_wt = soma_rt = 0
    n = len(processos)

    print("\nMétricas dos Processos")
    print("-" * 55)
    print(f"{'Proc':<6}{'AT':<6}{'PT':<6}{'TAT':<6}{'WT':<6}{'RT':<6}")
    print("-" * 55)

    for p in processos:
        tat = p.tempo_fim - p.tempo_chegada               # Turnaround Time
        wt = tat - p.tempo_execucao                          # Waiting Time
        rt = (p.tempo_inicio - p.tempo_chegada) if p.tempo_inicio is not None else 0  # Response Time

        soma_tat += tat
        soma_wt += wt
        soma_rt += rt

        print(f"{p.id_processo:<6}{p.tempo_chegada:<6}{p.tempo_execucao:<6}{tat:<6}{wt:<6}{rt:<6}")

    print("-" * 55)
    print(f"{'Médias':<18} {soma_tat/n:.2f}   {soma_wt/n:.2f}   {soma_rt/n:.2f}")

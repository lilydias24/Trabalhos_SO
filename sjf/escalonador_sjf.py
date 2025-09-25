import collections

# Classe que implementa o escalonador SJF (Shortest Job First) com preempção
class Escalonador_sjf:
	def __init__(self, processos):
		self.todos_processos = sorted(processos, key=lambda p: p.tempo_chegada)
		self.processos_disponiveis = []  # lista, pois precisamos ordenar por tempo_restante
		self.processo_em_execucao = None
		self.tempo_atual = 0
		self.processos_concluidos = []

	def simular_sjf_com_preempcao_com_tabela(self):
		print("--- Simulação SJF Preemptivo ---")
		print("{:<5} | {:<22} | {:<20} | {:<20} | {:<20}".format(
			"Tempo", "Evento", "Em Execução", "Fila de Prontos", "Tempos Restantes"
		))
		print("-" * 115)

		while self.todos_processos or self.processos_disponiveis or self.processo_em_execucao:
			evento = ""

			# 1. Adiciona processos que chegaram no tempo_atual à fila de prontos
			while self.todos_processos and self.todos_processos[0].tempo_chegada <= self.tempo_atual:
				processo = self.todos_processos.pop(0)
				self.processos_disponiveis.append(processo)
				evento += f"Chegada {processo.id_processo} "

			# 2. Ordena a fila de prontos pelo tempo_restante (SJF)
			self.processos_disponiveis.sort(key=lambda p: p.tempo_restante)

			# 3. Preempção: se há processo mais curto que o atual, troca
			if self.processos_disponiveis:
				if (self.processo_em_execucao is None or
					self.processos_disponiveis[0].tempo_restante < self.processo_em_execucao.tempo_restante):
					if self.processo_em_execucao:
						# Preempção: devolve o processo atual para a fila
						self.processos_disponiveis.append(self.processo_em_execucao)
						evento += f"Preempção {self.processo_em_execucao.id_processo} "
					self.processo_em_execucao = self.processos_disponiveis.pop(0)
					if self.processo_em_execucao.tempo_inicio is None:
						self.processo_em_execucao.tempo_inicio = self.tempo_atual
					evento += f"Início {self.processo_em_execucao.id_processo} "

			# 4. Executa o processo
			if self.processo_em_execucao:
				self.processo_em_execucao.tempo_restante -= 1
				# 5. Verifica se o processo terminou
				if self.processo_em_execucao.tempo_restante == 0:
					self.processo_em_execucao.tempo_fim = self.tempo_atual + 1
					evento += f"Fim {self.processo_em_execucao.id_processo} "
					self.processos_concluidos.append(self.processo_em_execucao)
					self.processo_em_execucao = None

			# 6. Formata a string de tempos restantes para a tabela
			tempos_restantes_str = ", ".join([
				f"{p.id_processo}: {p.tempo_restante}" for p in self.processos_disponiveis
			] + ([f"{self.processo_em_execucao.id_processo}: {self.processo_em_execucao.tempo_restante}" ] if self.processo_em_execucao else []))

			processo_atual_id = self.processo_em_execucao.id_processo if self.processo_em_execucao else "(Ocioso)"

			print("{:<5} | {:<22} | {:<20} | {:<20} | {:<20}".format(
				self.tempo_atual, evento, processo_atual_id,
				str(self.processos_disponiveis), tempos_restantes_str
			))

			self.tempo_atual += 1

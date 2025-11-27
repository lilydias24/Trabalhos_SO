import json
import os
from cores import Cores, colorir

# Caminho para o arquivo de configuração
CONFIG_FILE = 'configuracao.json'

def carregar_configuracao():
    """Lê e retorna o dicionário de configurações do arquivo JSON."""
    if not os.path.exists(CONFIG_FILE):
        print(colorir(f"\n❌ ERRO: Arquivo de configuração '{CONFIG_FILE}' não encontrado!", Cores.VERMELHO))
        print(colorir("Garanta que o arquivo esteja na pasta raiz do projeto.", Cores.VERMELHO))
        return {
            "limite_tempo_processo": 50,
            "taxas_interrupcao": {
                "Teclado": 0.15,
                "Impressora": 0.25,
                "Disco Rígido": 0.35
            }
        }

    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            print(colorir(f"\n✅ Configurações carregadas com sucesso de '{CONFIG_FILE}'.", Cores.VERDE))
            return config
    except json.JSONDecodeError:
        print(colorir(f"\n❌ ERRO: O arquivo '{CONFIG_FILE}' está mal formatado.", Cores.VERMELHO))
        return {}
    except Exception as e:
        print(colorir(f"\n❌ ERRO Desconhecido ao ler o arquivo de configuração: {e}", Cores.VERMELHO))
        return {}

# Variável global que será carregada
CONFIG = carregar_configuracao()
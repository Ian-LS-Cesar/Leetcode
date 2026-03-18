import os
from pathlib import Path

def listar_arquivos(caminho_arquivo: str):
    entries = os.listdir(caminho_arquivo)
    for entry in entries:
        caminho_inteiro = os.path.join(caminho_arquivo, entry)
        if os.path.isfile(caminho_inteiro) and Path(caminho_inteiro).stem != "organizador_arquivos":
            criar_pasta(caminho_inteiro)
            mover_arquivo(caminho_inteiro, criar_pasta(caminho_inteiro))


def criar_pasta(nome_arquivo):
    nome_pasta = Path(nome_arquivo).stem
    try:
        os.mkdir(nome_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso!")
    except FileExistsError:
        print(f"Pasta '{nome_pasta}' já existe!")
    except OSError as e:
        print(f"Erro criando pasta: {e}")
    return Path(nome_pasta)

def mover_arquivo(caminho_inteiro: str, caminho_pasta: Path):
    arquivo = Path(caminho_inteiro)
    pasta_destino = Path(caminho_pasta)

    pasta_destino.mkdir(parents=True, exist_ok=True)
    caminho_destino = pasta_destino / arquivo
    try:
        arquivo.rename(caminho_destino)
        print(f"Arquivo movido para pasta com sucesso!")
    except OSError as e:
        print("Erro ao mover o arquivo.")

listar_arquivos('.')
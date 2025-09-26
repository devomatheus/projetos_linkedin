from pathlib import Path
import tempfile


def escrita_atomica(path: Path, data: str, encoding="utf-8"):
    """
    Escreve dados em um arquivo de forma atômica:
    - Cria um arquivo temporário no mesmo diretório
    - Escreve nele
    - Substitui o destino final com replace()
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)  # garante que o diretório existe

    # cria arquivo temporário no mesmo diretório do destino
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=path.name, suffix=".tmp")
    tmp_path = Path(tmp_name)

    try:
        with open(fd, "w", encoding=encoding) as tmp_file:
            tmp_file.write(data)

        # substitui de forma atômica.
        if path.exists():
            path.unlink()  # remove destino se já existe
        tmp_path.rename(path)
    finally:
        # se algo der errado, remove o temporário
        if tmp_path.exists():
            tmp_path.unlink()

# --- Exemplo de uso ---
destino = Path("saida/relatorio.txt")
escrita_atomica(destino, "Relatório atualizado com segurança ✔")
print(f"Arquivo escrito em {destino.resolve()}")

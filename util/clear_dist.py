import os

if __name__ == "__main__":
    diretorio_superior = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dist'))

    arquivos_png = os.listdir(diretorio_superior)
    qtd_arquivos = len(arquivos_png)

    for arquivo in arquivos_png:
        if arquivo.endswith(".png"):
            caminho_arquivo = os.path.join(diretorio_superior, arquivo)
            os.remove(caminho_arquivo)

    print(f"Remoção concluída! {qtd_arquivos} arquivos png foram deletados")
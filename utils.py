import os
import zipfile
import shutil

def extrair_zip(caminho_zip, pasta_destino):
    if os.path.exists(pasta_destino):
        shutil.rmtree(pasta_destino)
    os.makedirs(pasta_destino, exist_ok=True)
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

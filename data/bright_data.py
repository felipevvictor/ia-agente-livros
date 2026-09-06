import json
import os
from datasets import load_dataset


def download_json():
  caminho_json = "./data/livros_amostra.json"

  # Verifica se o arquivo JÁ EXISTE. Se existir, ele encerra a função na hora
  # e NÃO faz o download novamente, evitando rodar a cada mensagem do chat.
  if os.path.exists(caminho_json):
    return

  os.makedirs("./data", exist_ok=True)

  # Baixa em modo streaming limitando a quantidade (ex: 15 livros)
  dataset = load_dataset(
      "BrightData/Goodreads-Books", split="train", streaming=True
  )
  dataset_limit = dataset.take(50)

  livros_amostra = []
  for row in dataset_limit:
    # Filtra e mantém apenas o que realmente importa para a IA ler
    livro_filtrado = {
        "Titulo": row.get("name"),
        "Autor": row.get("author"),
        "Genero": row.get("genres"),
        "Descricao": row.get("summary"),
    }
    livros_amostra.append(livro_filtrado)

  # Salva o JSON limpo e compacto
  with open(caminho_json, "w", encoding="utf-8") as f:
    json.dump(livros_amostra, f, ensure_ascii=False, indent=2)
import json
import requests
import streamlit as st
import data.bright_data as dw

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:3b"

# Executa o download apenas se o arquivo ainda não existir
dw.download_json()

# Carregando os arquivos de dados e contexto
try:
  with open("./data/livros_amostra.json", "r", encoding="utf-8") as amostra:
    dados_brutos = json.load(amostra)
    bright_data = json.dumps(dados_brutos, ensure_ascii=False, indent=2)
except FileNotFoundError:
  bright_data = "Dados do BrightData não encontrados."

try:
  with open("./data/livros.txt", "r", encoding="utf-8") as arquivos:
    livros = arquivos.read()
except FileNotFoundError:
  livros = "Lista de livros não encontrada."

try:
  with open("./data/persona.txt", "r", encoding="utf-8") as arquivo:
    persona = arquivo.read()
except FileNotFoundError:
  persona = "Dados de persona não encontrados."

# ==== System Prompt ===

SYSTEM_PROMPT = """Você é a BiblioTech, uma auxiliadora para recomendar livros para amantes da leitura. 
Você possui acesso a uma base de dados de livros em [BrightData]. Sempre consulte esses dados para responder sobre livros específicos.

OBJETIVO:
Recomendar livros com base na persona dos leitores e nos dados fornecidos.

REGRAS:
- Não sugira ou recomende preços nos livros
- Não envie links de compras
- Não substitui profissionais para análise textual e reconhecimentos técnicos
- Não responda nada além de recomendação ou assuntos pertinentes a livros
"""

# ==== CHAMAR OLLAMA ======


def perguntar(msg):
  prompt_completo = f"""
{SYSTEM_PROMPT}

---
CONTEXTO E DADOS DE REFERÊNCIA:
[BrightData]:
{bright_data}

[Livros Disponíveis]:
{livros}

[Personas]:
{persona}
---

Usuário: {msg}
"""

  try:
    r = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt_completo, "stream": False},
    )

    if r.status_code != 200:
      return f"Erro na API do Ollama (Status {r.status_code}): {r.text}"

    resposta_json = r.json()
    return resposta_json.get(
        "response", f"Resposta em formato inesperado: {resposta_json}"
    )

  except Exception as e:
    return f"Erro de conexão ao tentar falar com o Ollama: {e}"


# === Interface ====

st.title("BiblioTech, sua melhor companhia para leitura!")

if pergunta := st.chat_input("Sua dúvida sobre livros..."):
  st.chat_message("user").write(pergunta)
  with st.spinner("Pensando..."):
    resposta_ia = perguntar(pergunta)
    st.chat_message("assistant").write(resposta_ia)
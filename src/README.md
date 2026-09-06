# Passo a passo de execução

## Setup do ollama

```
# 1. Instalar o Ollama
# 2. Baixar um modelo
ollama pull llama 3.2 ou instalar diretamente no app Ollama

#3. Testar se funciona
ollama run llama3.2 "Olá"
```

## Código completo

todo o código-fonte no arquivo `app.py`

## Como Rodar

```bash
# Instalar dependências
python -m pip install streamlit pandas requests 

# Garantir que o ollama está rodando
ollama serve

# Rodar a aplicação
python -m streamlit run ".\src\app.py"
```
## Evidencia da execução


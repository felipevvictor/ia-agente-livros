# Avaliação e Métricas

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar recomendações referente a um genêro especifico e receber o resultado esperado |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do usuario? | Sugerir livros que fazem sentido |

---

## Cenários de Teste

Testes para validar o agente:

### Teste 1: Consulta de livros
- **Pergunta:** "Quais livros são para iniciantes em filosofia"
- **Resposta esperada:** Valor baseado no `Livros.txt` e `BrightData.py`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual livro você recomenda para mim?"
- **Resposta esperada:** Livro compatível com o perfil do cliente
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de livros
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual livro de ação é mais vendido"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- Pergunta dentro do escopo
- Perfil e tom de voz do agente: Testado com o agente gpt e llama3.2:3b, onde o GPT "veste a camisa" da atuação incluindo o tom de voz
- O perfil com llama não obteve o tom de voz adequado, mas a memória e velocidade de processamento é bem mais rápido
- No modelo llama os arquivos traduzidos pela API nem sempre são lidos corretamente

**O que pode melhorar:**
- Pergunta fora do escopo
- Base de conhecimento
---
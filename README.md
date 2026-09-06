# 📚 Agente Inteligente de Análise de Livros com IA Generativa

Agente conversacional que utiliza **IA Generativa** para analisar, recomendar e responder perguntas sobre livros, combinando um modelo de linguagem (LLM) com uma base de conhecimento própria.

> Projeto desenvolvido a partir do lab **[dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)**, da Digital Innovation One, adaptado do domínio financeiro original para o domínio de **livros e literatura**.

---

## 📖 Sobre o projeto

Assistentes de IA estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**, capazes de:

- **Antecipar necessidades** do leitor, não apenas responder perguntas
- **Personalizar** recomendações com base no perfil e no histórico de leitura
- **Cocriar** experiências literárias de forma consultiva (ex: "quero algo parecido com X, mas mais leve")
- **Garantir confiabilidade** nas respostas, evitando alucinações sobre autores, sinopses e dados de obras

Este repositório documenta e implementa um protótipo desse agente, aplicado a um **acervo de livros**.

---

## 🗂️ Estrutura do repositório

```
ia-agente-livros/
│
├── 📄 README.md                  # Este arquivo
│
├── 📁 data/                      # Base de conhecimento (dados de livros, acervo, histórico)
│
├── 📁 docs/                      # Documentação do agente
│   ├── 01-documentacao-agente.md # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md   # Estratégia e estrutura dos dados
│   ├── 03-prompts.md             # System prompt e exemplos de interação
│   ├── 04-metricas.md            # Avaliação e métricas de qualidade
│   └── 05-pitch.md               # Roteiro de apresentação do projeto
│
├── 📁 src/                       # Código-fonte da aplicação (agente + interface)
│
└── 📁 examples/                  # Prints da aplicação rodando
```

---

## 🧠 Como o agente funciona

1. **Entrada do usuário** — uma pergunta ou pedido sobre livros (ex: "me indique um livro parecido com Sapiens").
2. **Consulta à base de conhecimento** — o agente busca informações relevantes em `data/` (acervo, sinopses, categorias, avaliações).
3. **Geração de resposta com IA** — o LLM combina o contexto recuperado com o *system prompt* definido em `docs/03-prompts.md` para gerar uma resposta personalizada e fundamentada.
4. **Resposta ao usuário** — via interface de chat (ex: Streamlit/Gradio), evitando respostas genéricas ou alucinadas.

Para detalhes de arquitetura, persona e regras de segurança contra alucinações, veja [`docs/01-documentacao-agente.md`](docs/01-documentacao-agente.md).

---

## 🚀 Como executar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/felipevvictor/ia-agente-livros.git
cd ia-agente-livros

# 2. Instalar dependências
python -m pip install streamlit pandas requests 

# 3. Garantir que o ollama está rodando
ollama serve

# 4. Rodar a aplicação
python -m streamlit run ".\src\app.py"
```

---

## 🛠️ Tecnologias sugeridas

| Categoria           | Ferramentas                                                                 |
| ------------------- | ---------------------------------------------------------------------------- |
| **LLMs**            | ChatGPT, Gemini, Claude, Ollama                                               |
| **Interface**       | Streamlit, Llama                                                             |                                               |
| **Dados**           | CSV / JSON com acervo de livros, sinopses, avaliações e perfis de leitura     |

---

## 📊 Avaliação

A qualidade das respostas do agente pode ser avaliada por métricas como:

- **Precisão/assertividade** das recomendações e informações sobre obras
- **Taxa de respostas seguras** (sem invenção de autores, títulos ou dados)
- **Coerência** com o perfil e as preferências do leitor

Veja detalhes em [`docs/04-metricas.md`](docs/04-metricas.md).

---

## 🤝 Contribuindo

Sugestões, issues e pull requests são bem-vindos. Para mudanças maiores, abra uma *issue* primeiro para discutir o que você gostaria de alterar.

---

## NOTE

Atualmente o projeto está estruturado com o modelo Llama que por sua vez, sendo leve e simples para rodar em qualquer máquina, apresentou um resultado
que poderia ser melhor. Pode ser alterado para outros modelos como GPT, porém, visando que é necessário ter um hardware compatível para não haver muitos travamentos

---

## 📄 Créditos

Este projeto tem origem no lab **[dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)** da [Digital Innovation One](https://www.dio.me/), adaptado por [@felipevvictor](https://github.com/felipevvictor) para o domínio de análise de livros.

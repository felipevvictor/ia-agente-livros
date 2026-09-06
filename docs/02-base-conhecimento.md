# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `livros_amostra.json` | API | Contextualizar informações via API para analisar informações de livros |
| `livros.txt` | TXT | Aumentar a quantidade de informações com dados em memória |
| `persona.txt` | TXT | Atribuir uma pequena base para recomendar livros com precisão |

---

## Adaptações nos Dados

> O projeto deve baixar um arquivo json e ler todas as informações mockadas

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos são carregados no início da sessão e incluídos no contexto do prompt, podendo forçar o agente a ler os dados do BrightData

### Como os dados são usados no prompt?
> Os dados devem ser consultados dinâmicamente, encontrando padrões pela API e txt

```
Informações de perfil ->  persona.txt
Livros recomendados -> livros.txt e livros_amostra.json

```

---

## Exemplo de Contexto Montado

A base de conhecimento é formatada em estilo tabela, porém, os usuários podem inserir texto corrido

```
Nome,Idade,Genero_Leitor,Personalidade,Livros_Lidos,Generos_Preferidos,Interesses_Gerais
"Carlos","23","Masculino","Reflexiva","A República | 1984 | Além do Bem e do Mal","Filosofia | Distopia","Política | Sociedade | História"
...
```

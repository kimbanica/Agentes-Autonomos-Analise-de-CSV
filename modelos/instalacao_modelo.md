# 🧠 Instalação do Modelo `mistral-7b-instruct-v0.1.Q5_K_M.gguf`

Este guia ensina como baixar o modelo **Mistral 7B Instruct (Q5_K_M)** no formato `.gguf` e integrá-lo ao seu projeto de agente autônomo.

---

## ✅ Pré-requisitos

- Conexão com a internet
- 8 GB ou mais de espaço em disco
- Python 3.10+
- Projeto com pasta `modelos/`

---

## 🔗 Link oficial

O modelo pode ser baixado a partir do Hugging Face:

👉 [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

---

## 📥 Etapas para baixar

1. Acesse o link acima.
2. Localize o arquivo chamado:

```
mistral-7b-instruct-v0.1.Q5_K_M.gguf
```

3. Clique no nome do arquivo para iniciar o download.
4. Após o download, mova o arquivo para dentro da pasta `modelos/` do seu projeto:

```
agente_csv/
└── modelos/
    └── mistral-7b-instruct-v0.1.Q5_K_M.gguf
```

---

## ⚙️ Exemplo de uso no código

```python
from langchain_community.llms import LlamaCpp

llm = LlamaCpp(
    model_path="./modelos/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
    temperature=0,
    max_tokens=512,
    n_ctx=2048,
    verbose=True
)

resposta = llm("Qual a capital do Brasil?")
print(resposta)
```

---

## ⚠️ Observações

- **Limite de contexto**: Este modelo suporta até **2048 tokens** no total (prompt + resposta). Perguntas longas ou arquivos CSV extensos podem exceder esse limite e causar erros.
- **Solução**: Reduza o número de linhas analisadas ou simplifique a pergunta para evitar exceder `n_ctx`.

---

## 🛑 Dica de segurança

> Evite versionar esse arquivo `.gguf` no GitHub, pois ele é muito grande. Mantenha-o fora do repositório (`.gitignore`) e oriente os colegas a baixarem manualmente conforme instruções acima.

---


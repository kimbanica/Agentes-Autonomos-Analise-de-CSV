# 🧠 Instalação do Modelo `mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf`

Este guia ensina como baixar o modelo **Mixtral 8x7B Instruct (Q5_K_M)** no formato `.gguf` e integrá-lo ao seu projeto de agente autônomo.

---

## ✅ Pré-requisitos

- Conexão com a internet
- 20 GB ou mais de espaço em disco
- Python 3.10+
- Projeto com pasta `modelos/`

---

## 🔗 Link oficial

O modelo pode ser baixado a partir do Hugging Face:

👉 [https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-GGUF](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-GGUF)

---

## 📥 Etapas para baixar

1. Acesse o link acima.
2. Localize o arquivo chamado:

```
mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf
```

3. Clique no nome do arquivo para baixar.
4. Após o download, mova o arquivo para dentro da pasta `modelos/` do seu projeto:

```
agente_csv/
└── modelos/
    └── mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf
```

---

## ⚙️ Exemplo de uso no código

```python
from langchain_community.llms import LlamaCpp

llm = LlamaCpp(
    model_path="./modelos/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf",
    temperature=0.7,
    max_tokens=512,
    n_ctx=32768,
    verbose=True
)

resposta = llm("Qual a capital do Brasil?")
print(resposta)
```

---

## ⚠️ Observações

- **Limite de contexto**: Embora o Mixtral suporte até 32.000 tokens, isso depende da sua máquina. Se ocorrer erro de memória ou tokens, tente reduzir `n_ctx` para 4096 ou 2048.
- **Velocidade**: A quantização Q5_K_M oferece bom equilíbrio entre desempenho e precisão.

---

## 🛑 Dica de segurança

> Evite versionar esse arquivo `.gguf` no GitHub, pois ele é grande. Mantenha fora do repositório e oriente os membros da equipe a baixarem manualmente conforme instruções acima.

---

📁 **Dica:** salve este arquivo como `docs/instalacao_modelo.md` no seu projeto.

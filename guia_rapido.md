# 📘 Guia Rápido para Executar o Projeto

## 1. Pré-requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- LangChain + langchain-community + langchain-experimental
- Modelo Mistral em `GGUF` no diretório `/modelos`

## 2. Execução

```bash
uvicorn main:app --reload --port 8080
```

## 3. Enviar arquivo via cURL

```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/perguntar/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'zip_file=@202401_NFs.zip' \
  -F 'pergunta=Qual é o fornecedor que teve maior montante recebido?'
```

A resposta será retornada em formato JSON.

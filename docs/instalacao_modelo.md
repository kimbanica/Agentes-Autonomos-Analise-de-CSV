# 🧠 Instruções para Baixar o Modelo Mistral (GGUF)

Este agente utiliza fallback para o modelo local `mistral-7b-instruct-v0.1.Q5_K_M.gguf` se a OpenAI estiver indisponível.

## 📥 Baixe o modelo
1. Acesse: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
2. Faça download do arquivo: `mistral-7b-instruct-v0.1.Q5_K_M.gguf`
3. Coloque o arquivo dentro da pasta `/modelos` do projeto.

## ⚠️ Atenção ao Contexto

Esse modelo suporta no máximo 2048 tokens por resposta. Evite perguntas muito longas ou com múltiplas instruções encadeadas.

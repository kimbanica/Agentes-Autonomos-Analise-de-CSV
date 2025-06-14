# Guia de Execução do Agente Autônomo - Análise de Arquivos CSV

Este guia descreve todas as etapas necessárias para executar localmente o projeto de agente autônomo com análise de arquivos CSV utilizando a FastAPI e modelos LLM (OpenAI e Mistral).

---

## 1. Acesso ao Repositório

1. Acesse o site [https://github.com](https://github.com).
2. Faça login com sua conta GitHub.
3. Acesse o repositório do projeto:
   ```
   https://github.com/kimbanica/Agentes-Autonomos-Analise-de-CSV
   ```
4. Clique no botão verde **"Code"** e depois em **"Download ZIP"**.

---

## 2. Preparação do Projeto

### 2.1. Descompactar o Projeto

- Extraia o conteúdo do ZIP em uma pasta local, por exemplo: `C:/Users/SeuNome/Agente_CSV/`

### 2.2. Acessar via Prompt de Comando

Abra o terminal (CMD ou PowerShell) e navegue até a pasta do projeto:

```bash
cd C:\Users\SeuNome\Agente_CSV
```

---

## 3. Arquivo `.env` com chave da OpenAI

Crie um novo arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Substitua `sua_chave_aqui` pela sua chave válida da OpenAI.

---

## 4. Instalar o Modelo Local (Mistral)

1. Baixe o modelo `mistral-7b-instruct-v0.1.Q5_K_M.gguf` do site oficial:
   - Acesse: [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
   - Faça login e aceite os termos.
   - Baixe a versão `Q5_K_M`.

2. Crie a pasta `modelos` na raiz do projeto e coloque o arquivo dentro dela:

```
Agentes-Autonomos-Analise-de-CSV/
├── modelos/
│   └── mistral-7b-instruct-v0.1.Q5_K_M.gguf
```

---

## 5. Criar Ambiente Virtual

```bash
python -m venv venv
```

### Ativar o Ambiente

**Windows PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
```

**CMD:**

```bash
venv\Scripts\activate.bat
```

---

## 6. Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 7. Rodar o Servidor

```bash
uvicorn main:app --reload --port 8080
```

Acesse no navegador:

```
http://127.0.0.1:8080/docs
```

---

## 8. Usar o Agente

1. Na interface FastAPI UI:
   - Faça upload do arquivo `.zip` contendo arquivos `.csv`
   - Insira a pergunta, como:
     > Qual fornecedor teve maior montante recebido?

2. Clique em **"Execute"**.

---

✅ O agente responderá com base nos dados do CSV usando OpenAI ou Mistral como fallback.

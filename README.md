# 🤖 Agente Autônomo para Análise de Arquivos CSV

Este projeto utiliza um agente inteligente que processa arquivos `.csv` compactados em `.zip`, responde a perguntas sobre os dados e realiza análise autônoma. Ele conta com fallback automático para um modelo local (Mistral) caso a cota da OpenAI seja excedida.

## 🚀 Como usar

1. Faça upload de um arquivo `.zip` contendo um ou mais arquivos `.csv`.
2. O agente extrai, analisa e responde automaticamente com base nos dados.
3. O sistema utiliza OpenAI se disponível. Caso contrário, ativa o modelo local `Mistral-7B`.

## 🔗 Documentação Complementar

- 📥 [Como configurar o modelo Mistral](docs/instalacao_modelo.md)
- 💡 [Exemplos de perguntas](docs/perguntas_exemplo.md)
- 🛠️ [Guia completo de execução](docs/Guia_Execucao_Agente_CSV)

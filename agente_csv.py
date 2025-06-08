import os
import zipfile
import tempfile
from langchain_community.llms import OpenAI, LlamaCpp
from langchain_experimental.agents import create_csv_agent
import traceback

def responder(arquivo_zip_path: str, pergunta: str) -> str:
    try:
        # Criar diretório temporário
        temp_dir = tempfile.mkdtemp()

        # Extrair o ZIP
        with zipfile.ZipFile(arquivo_zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Buscar CSV
        csv_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith('.csv')]
        if not csv_files:
            return "Nenhum arquivo CSV encontrado no ZIP."
        caminho_csv = csv_files[0]

        # Prefixo para instruir o agente a responder em português
        prefixo_portugues = """
        Você é um assistente de dados que fala apenas português.
        Sempre responda com base nos dados da tabela e forneça a resposta em linguagem natural, clara e concisa.
        Quando possível, destaque o valor numérico com 'R$'e o nome da coluna entre aspas. 
        Exemplo: O maior valor está na coluna 'VALOR NOTA FISCAL' e é R$ 1.292.418,75. 
        """

        try:
            # Tenta com OpenAI
            llm = OpenAI(temperature=0)
            agente = create_csv_agent(
                llm,
                caminho_csv,
                verbose=True,
                prefix=prefixo_portugues,
                allow_dangerous_code=True
            )
            resposta = agente.run(pergunta)
            return resposta

        except Exception as e:
            if "insufficient_quota" in str(e) or "Error code: 429" in str(e):
                print("Fallback: Usando modelo local Mistral.")

                llm = LlamaCpp(
                    model_path="./modelos/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
                    temperature=0,
                    max_tokens=1024,
                    n_ctx=2048,
                    verbose=False
                )

                agente = create_csv_agent(
                    llm,
                    caminho_csv,
                    verbose=True,
                    prefix=prefixo_portugues,
                    agent_type="openai-tools",
                    allow_dangerous_code=True
                )

                resposta = agente.run(pergunta)
                return resposta
            else:
                raise e

    except Exception as e:
        print(traceback.format_exc())
        return f"Erro ao processar pergunta: {str(e)}"

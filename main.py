from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
import shutil
import traceback
import tempfile
import os

from agente_csv import responder

app = FastAPI(title="Agente Inteligente de CSV", description="API em português com tema dourado")

# Monta os arquivos estáticos (JS/CSS personalizados)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "API está rodando com agente autônomo Mistral e fallback OpenAI."}

# Personalização da interface Swagger
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Documentação da API - Agente CSV",
        swagger_js_url="/static/swagger_custom.js",
        swagger_css_url="/static/swagger_custom.css"
    )

# Endpoint principal
@app.post("/perguntar/")
async def perguntar(zip_file: UploadFile = File(...), pergunta: str = Form(...)):
    temp_dir = tempfile.mkdtemp()

    try:
        zip_path = os.path.join(temp_dir, zip_file.filename)
        with open(zip_path, "wb") as f:
            f.write(await zip_file.read())

        resposta = responder(zip_path, pergunta)
        return {"resposta": resposta}

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"erro": "Erro interno no servidor. Detalhes: " + str(e)}
        )
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

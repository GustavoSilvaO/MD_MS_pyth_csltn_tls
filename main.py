from fastapi import FastAPI
from pydantic import BaseModel
from service.teste import hello_world

app = FastAPI(title="MindDesk - Agente Tools MVP")

# Precisamos espelhar o que o Orquestrador vai mandar para não dar erro 422
class ToolPayload(BaseModel):
    query: str
    tenant_id: int
    user_id: str = "N/A"
    role: str = "N/A"
    openai_api_key: str = ""
    supabase_url: str = ""
    supabase_key: str = ""

@app.post("/api/v1/executar")
async def executar_acao(payload: ToolPayload):

    resultado = hello_world()

    return {
        "answer": resultado
    }
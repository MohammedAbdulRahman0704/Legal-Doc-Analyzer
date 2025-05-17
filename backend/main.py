from fastapi import FastAPI, Form
import requests
from typing import Dict

app = FastAPI(
    title="IntelliDoc Legal Analyzer API",
    description="Uses LLaMA2 (via Ollama) to extract summaries, key clauses and named entities from legal and policy documents.",
    version="2.0.0"
)

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Replace with your Ollama API URL
OLLAMA_MODEL = "llama2"  # Replace with your Ollama model name
OLLAMA_API_KEY = "your_api_key"  # Replace

def call_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.RequestException as e:
        return f"Error contacting LLM: {str(e)}"
    
@app.post("/analyze")
def analyze_legal(
    text: str = Form(...),
    summary: bool = Form(True),
    clauses: bool = Form(True),
    entities: bool = Form(True),
) -> Dict[str, str]:
    prompts = {}
    if summary:
        prompts["summary"] = f"Summarize the following legal text:\n\n{text}"
    if clauses:
        prompts["clauses"] = f"Extract key clauses from the following legal text:\n\n{text}"
    if entities:
        prompts["entities"] = f"Extract named entities from the following legal text:\n\n{text}"
    
    results = {section: call_llm(prompt) for section, prompt in prompts.items()}
    return {"results": results}
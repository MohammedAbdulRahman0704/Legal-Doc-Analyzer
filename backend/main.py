from fastapi import FastAPI, Form
import requests

app = FastAPI()

# Call LLM through Ollama (local)
def call_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False}
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    """
    Analyzes the input text using prompts for:
    - Summary
    - Key Clauses
    - Named Entities
    """
    prompts = {
        "summary": f"Summarize this legal document:\n\n{text}",
        "clauses": f"Extract key clauses from this legal text (e.g., Termination, Payment, Liability):\n\n{text}",
        "entities": f"Extract all named entities (e.g., parties, locations, dates):\n\n{text}"
    }

    results = {key: call_llm(prompt) for key, prompt in prompts.items()}
    return results
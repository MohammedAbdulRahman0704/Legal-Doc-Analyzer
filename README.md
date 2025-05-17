```markdown
# IntelliDoc Legal Analyzer API

A powerful web application leveraging **LLaMA2** (via **FastAPI** and **Ollama**) to analyze legal documents (PDF or text).  
Get **Summaries**, **Key Clauses**, and **Named Entities** extracted from your documents with **AI-powered NLP**.

---

## Features

- ✅ Upload and display PDF files directly in your browser  
- ✅ Extract and analyze legal content with LLaMA2 AI model  
- ✅ Input legal text directly as an alternative to PDFs  
- ✅ Categorized analysis: **Summary**, **Key Clauses**, **Named Entities**  
- ✅ Clean, intuitive, and collapsible UI built with Streamlit  
- ✅ Robust FastAPI backend with prompt engineering optimized for legal context  

---

## Project Structure

```

legal-analyzer/
├── backend/
│   └── main.py         # FastAPI backend with LLaMA2 prompt logic
├── frontend/
│   └── app.py          # Streamlit frontend for file upload & visualization
├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn requests streamlit PyPDF2
```

---

## LLaMA2 & Ollama Setup

Make sure [Ollama](https://ollama.com) is installed and the LLaMA2 model is downloaded:

```bash
ollama run llama2
```

---

## Running the Application

### Step 1: Start Backend Server

```bash
cd backend
uvicorn main:app --reload
```

> **Keep this terminal running** — it serves the AI-powered API.

---

### Step 2: Start Frontend UI (In a New Terminal)

```bash
cd frontend
streamlit run app.py
```

---

### Step 3: Use the App!

* Upload a **PDF document** (preview it instantly)
* Or paste **legal text**
* Click **Analyze**
* Explore the categorized AI insights:

  * Summary
  * Key Clauses
  * Named Entities

---

## Example Screenshot

*(Add UI screenshots here to showcase the app in action)*

---

## Customization Tips

* **Change Model**: Update `"model": "llama2"` in `backend/main.py`
* **Modify Prompts**: Edit prompts in the `prompts` dictionary for tailored analysis
* **Enhance UI**: Improve or extend features using Streamlit components in `frontend/app.py`

---

## Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/) — backend API framework
* [Streamlit](https://streamlit.io/) — interactive frontend UI
* [Ollama](https://ollama.com/) — LLaMA2 model hosting and serving
* [Meta LLaMA2](https://ai.meta.com/llama/) — foundational AI model
* [PyPDF2](https://pypi.org/project/PyPDF2/) — PDF parsing

---

## License & Disclaimer

This project is intended for **educational and research purposes only**.
AI-generated legal insights should always be **verified by qualified legal professionals** before use.

---
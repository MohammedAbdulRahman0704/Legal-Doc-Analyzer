Sure! Here's the **updated `README.md`** including instructions to set up a **Python virtual environment (`venv`)** before running the backend and frontend:

---

```markdown
# IntelliDoc Legal Analyzer API

A powerful web application that uses **LLaMA2 (via FastAPI and Ollama)** to analyze legal documents (PDF or text).  
Get **Summaries**, **Key Clauses**, and **Named Entities** extracted from your documents using **AI-powered NLP**.

---

## 🚀 Features

- ✅ Upload and display PDF files directly in the browser
- ✅ Extract and analyze legal content using LLaMA2
- ✅ Text input alternative for non-PDF content
- ✅ Categorized analysis: Summary, Key Clauses, Named Entities
- ✅ Clean, collapsible UI with Streamlit
- ✅ FastAPI backend with prompt engineering for legal context

---

## 🗂️ Project Structure

```

legal-analyzer/
├── backend/
│   └── main.py         # FastAPI backend with LLaMA2 prompts
├── frontend/
│   └── app.py          # Streamlit frontend for file upload and visualization
├── requirements.txt
├── README.md

````

---

## Requirements

### Create and Activate Virtual Environment

Before running the application, it's highly recommended to use a virtual environment:

```bash
# Step 1: Create virtual environment
python -m venv venv

# Step 2: Activate the environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
````

### 🧩 Install Required Packages

After activation, install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn requests streamlit PyPDF2
```

---

## 🧠 LLaMA2 & Ollama Setup

Ensure [Ollama](https://ollama.com) is installed and LLaMA2 is downloaded:

```bash
# Download and run LLaMA2 model
ollama run llama2
```

---

## ▶️ How to Run the Project

### Step 1: Start the Backend Server

```bash
cd backend
uvicorn main:app --reload
```

⚠️ **Keep this terminal running** — it serves the LLaMA2-powered API.

---

### Step 2: Start the Frontend (New Terminal)

Open a **new terminal** while the backend is still running:

```bash
cd frontend
streamlit run app.py
```

---

### Step 3: Use the Application

* Upload a **PDF document** (displayed directly)
* Or paste **legal text**
* Click **Analyze**
* View categorized insights:

  * 📄 Summary
  * 📌 Key Clauses
  * 🔍 Named Entities

---

## 🧪 Example Screenshot

*(You can add UI screenshots here for a better demo)*

---

## 🔧 Customization

* **Model Name**: Modify `"model": "llama2"` in `main.py`
* **Prompts**: Customize in the `prompts` dictionary for different tasks
* **UI**: Enhance layout or features via Streamlit components

---

## 🛠 Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [Ollama](https://ollama.com/)
* [Meta LLaMA2](https://ai.meta.com/llama/)
* [PyPDF2](https://pypi.org/project/PyPDF2/)

---

## 📜 License

This project is for educational and research use only.
AI-generated insights should be verified by qualified legal professionals.

---
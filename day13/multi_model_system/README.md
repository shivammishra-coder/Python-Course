# 🤖 AI Interaction Orchestrator (CLI-Based)

This project provides a **command-line interface (CLI)** to run an AI-powered **interaction orchestrator**.

It allows users to input a **discussion topic**, and the system processes it through a structured orchestration pipeline to generate results.

---

## 🚀 Features

### ✅ CLI-Based Input
- Accepts user input directly from terminal  
- Simple and interactive  

---

### ✅ Configuration Validation
- Ensures required configurations are set before execution  
- Prevents runtime failures  

---

### ✅ Orchestration Engine
- Uses `InteractionOrchestrator` to process topics  
- Can support multi-agent or pipeline-based workflows  

---

### ✅ Structured JSON Output
- Outputs results in clean JSON format  
- Easy to integrate with other systems  

---

### ✅ Error Handling
- Handles:
  - Missing configuration  
  - Empty input  
  - Runtime errors  

---

## 🛠️ Tech Stack

- Python  
- Custom Orchestrator Module  
- JSON for structured output  

---

## 📦 Installation

Clone the repository and install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup

Make sure your configuration is properly set.

The project uses:

```python
from config import validate_config
```

Ensure:
- API keys or environment variables are configured  
- `validate_config()` passes successfully  

---

## ▶️ How to Run

Run the script:

```bash
python main.py
```

---

## 🧪 Example

### Input:
```
Enter discussion topic: Future of AI in healthcare
```

### Output:
```json
{
  "summary": "...",
  "insights": [...],
  "recommendations": [...]
}
```

---

## ⚙️ Code Flow

1. Validate configuration  
2. Take user input  
3. Initialize orchestrator  
4. Execute orchestration pipeline  
5. Return JSON result  

---

## 📂 Project Structure

```
.
├── main.py                             # Entry point
├── config.py                           # Configuration validation
├── orchestrator/
│   └── interaction_orchestrator.py     # Core orchestration logic
├── README.md
└── requirements.txt
```

---

## ⚠️ Error Handling

### Empty Topic
```json
{
  "error": "Topic cannot be empty."
}
```

### Configuration Error
```json
{
  "error": "Missing API key..."
}
```

---

## 🧠 Use Cases

- AI discussion systems  
- Multi-agent orchestration  
- Research assistants  
- Automated brainstorming tools  

---

## 💡 Future Improvements

- Add web interface (Streamlit / FastAPI)  
- Add logging & monitoring  
- Support multiple input formats  
- Integrate with external APIs  
- Add streaming responses  

---

## ⚡ Notes

- Output is always in JSON format  
- Designed for extensibility with custom orchestrators  
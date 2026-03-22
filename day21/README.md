# 🧠 Multi-Agent SRS Analyzer (LangGraph + Gemini)

This project builds a **multi-agent AI system** using:

- LangGraph (workflow orchestration)  
- LangChain  
- Google Gemini (LLM)  

The system automatically analyzes a **Software Requirement Specification (SRS)** and generates:

- 📄 Document summary  
- 📋 Requirements  
- ⚠️ Risks  
- 🏗️ Architecture  
- 🧪 Test cases  
- 👨‍💻 Human-reviewed final report  

---

## 🚀 Features

### ✅ Multi-Agent Architecture
Each task is handled by a dedicated AI agent:

- Document Analyzer  
- Requirement Extractor  
- Risk Analyzer  
- Architecture Designer  
- Test Case Generator  

---

### ✅ Parallel Processing
- Requirements & Risks generated in parallel  
- Architecture & Test Cases derived from requirements  

---

### ✅ Human-in-the-Loop
- User reviews intermediate results  
- Adds feedback before final report  

---

### ✅ Automated Report Generation
- Combines all outputs into a structured final report  

---

## 🛠️ Tech Stack

- Python  
- LangGraph  
- LangChain  
- Google Gemini (`gemini-2.5-flash`)  

---

## 📦 Installation

Install dependencies:

```bash
pip install langchain langgraph langchain-google-genai
```

---

## 🔑 Setup

Set your Gemini API key:

```bash
export GOOGLE_GEMINI_KEY=your_api_key
```

Or in Python:

```python
import os
os.environ["GOOGLE_GEMINI_KEY"] = "your_api_key"
```

---

## ▶️ How It Works

### Workflow Steps:

1. **Input SRS**
2. **Analyze Document**
3. **Parallel Execution:**
   - Extract Requirements  
   - Identify Risks  
4. **Generate:**
   - Architecture  
   - Test Cases  
5. **Merge Results**
6. **Human Review**
7. **Generate Final Report**

---

## 🔄 Workflow Architecture

```
input → analyzer
           ↓
   ┌───────────────┬───────────────┐
   ↓               ↓
requirements     risks
   ↓
┌───────────────┬───────────────┐
↓               ↓
architecture   test_cases
   ↓               ↓
       merge ←─────┘
          ↓
     human_review
          ↓
     final_report → END
```

---

## 🧪 Example Use Case

### Input:
```
Online Food Delivery System SRS
```

### Output Includes:
- Key features summary  
- Functional & non-functional requirements  
- Project risks  
- Suggested architecture  
- Test cases  
- Human-reviewed final report  

---

## 📂 Project Structure

```
.
├── main.py / notebook.ipynb   # Workflow implementation
├── README.md                 # Documentation
└── requirements.txt          # Dependencies
```

---

## 🧠 Key Concepts

- Multi-Agent Systems  
- LangGraph Workflows  
- Prompt Engineering  
- Human-in-the-loop AI  
- Automated Software Analysis  

---

## ⚠️ Important Notes

- Requires Gemini API key  
- Human input required during execution  
- Output depends on LLM quality  

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run script / notebook  
4. Provide human feedback when prompted  
5. View final generated report  

---

## 🎯 Use Cases

- Software requirement analysis  
- Project planning automation  
- AI-assisted documentation  
- Engineering workflow automation  

---

## 💡 Future Improvements

- Add UI (Streamlit / Web App)  
- Store reports in database  
- Support multiple SRS documents  
- Add evaluation metrics  
- Integrate with Jira / project tools  
# 🤖 Fallback AI Agent (LangChain + Groq)

This project demonstrates a **tool-using AI agent with fallback logic**, built using:

- LangChain  
- Groq (LLaMA 3.1 model)  

The agent follows a **step-by-step reasoning process**:
1. Try internal data source  
2. Detect failure  
3. Automatically switch to backup source  

---

## 🚀 Features

### ✅ Primary Tool (Internal DB)
- Simulates internal stock price database  
- Currently returns failure (`Database Timeout`)  

---

### ✅ Backup Tool (Web Search)
- Acts as fallback mechanism  
- Returns stock price when primary fails  

---

### ✅ Intelligent Fallback Logic
- Agent checks tool output  
- Detects failure conditions  
- Switches to backup tool automatically  

---

### ✅ Transparent Reasoning
- Captures:
  - Actions (tool calls)  
  - Observations (tool outputs)  
  - Final answer  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Groq API (`llama-3.1-8b-instant`)  

---

## 📦 Installation

Install dependencies:

```bash
pip install langchain_community langchain_groq
```

---

## 🔑 Setup

If using **Google Colab**:

```python
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API")
```

Or set manually:

```bash
export GROQ_API_KEY=your_api_key
```

---

## ▶️ How It Works

1. User asks for stock price  
2. Agent calls:
   ```
   get_internal_stock_price
   ```
3. Receives error:
   ```
   Database Timeout
   ```
4. Agent switches to:
   ```
   search_public_web
   ```
5. Returns final answer  

---

## 🧪 Example

### Input:
```
What is the current stock price of Apple?
```

### Reasoning:
```
Action: get_internal_stock_price | Input: Apple  
Observation: Error: Database Timeout  

Action: search_public_web | Input: Apple stock price  
Observation: Apple stock is at $170  
```

### Output:
```
Apple stock is at $170
```

---

## 📊 Debugging & Reasoning Trace

The agent logs:

- Tool calls (`tool_calls`)  
- Tool outputs (`ToolMessage`)  
- Final AI response  

Example extraction:

```python
for msg in messages:
    if hasattr(msg, "tool_calls"):
        ...
```

---

## 📂 Project Structure

```
.
├── main.py / notebook.ipynb   # Agent implementation
├── README.md                 # Documentation
└── requirements.txt          # Dependencies
```

---

## 🧠 Key Concepts

- Tool Calling  
- Fallback Strategies  
- ReAct Reasoning  
- Error Handling in Agents  
- Multi-step Decision Making  

---

## ⚠️ Important Notes

- Agent must NOT call both tools simultaneously  
- Must wait for observation before fallback  
- Fallback triggered only on failure keywords  

---

## 🎯 Use Cases

- Fault-tolerant AI systems  
- Financial assistants  
- API fallback handling  
- Production-grade agent design  

---

## 💡 Future Improvements

- Real stock API integration  
- Add retry mechanism  
- Add multiple fallback layers  
- Logging & monitoring  

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run script / notebook  
4. Enable debug mode to see reasoning  
# 🤖 Tool-Calling AI Agent (LangChain + Groq)

This project demonstrates a **tool-using AI agent** built with:

- LangChain  
- Groq (LLaMA 3.1 model)  

The agent is designed to handle **SaaS financial operations**, such as:

- 💰 Refund a transaction  
- ❌ Cancel a subscription  

It uses structured reasoning (**ReAct pattern**) to decide which tool to call.

---

## 🚀 Features

### ✅ Tool-Based Agent
- Uses LangChain tools  
- Dynamically selects correct tool based on user input  

---

### ✅ Refund Tool
Handles one-time transaction refunds.

**Input:**
- `transaction_id`

**Example:**
```
TXN991
```

---

### ✅ Subscription Cancellation Tool
Stops recurring payments.

**Input:**
- `email_id`

**Example:**
```
john@email.com
```

---

### ✅ ReAct Reasoning Pattern
Agent follows:

```
Thought → Action → Final Answer
```

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Groq API (`llama-3.1-8b-instant`)  
- Wikipedia API (optional utility)  

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

1. User provides a request  
2. Agent analyzes intent  
3. Extracts required parameters:
   - `transaction_id` OR  
   - `email_id`  
4. Calls appropriate tool  
5. Returns final response  

---

## 🧪 Test Cases

### 🔹 Cancel Subscription

**Input:**
```
I don't want to use your software anymore, stop charging john@email.com.
```

**Expected Tool Call:**
```
cancel_subscription(email_id="john@email.com")
```

---

### 🔹 Refund Transaction

**Input:**
```
My last charge of $50 on ID #TXN991 was a mistake, give it back.
```

**Expected Tool Call:**
```
refund_order(transaction_id="TXN991")
```

---

## 📊 Output Inspection

To verify tool usage:

```python
print(result['messages'][0].tool_calls)
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

- Tool Calling in LLMs  
- ReAct Agents  
- Prompt Engineering  
- Structured Output Parsing  
- API Integration  

---

## ⚠️ Important Notes

- Agent strictly relies on tools (no internal assumptions)  
- Ensure correct parameter extraction from user input  
- Tool calls can be inspected via `tool_calls`  

---

## 🎯 Use Cases

- Customer support automation  
- SaaS billing systems  
- AI-powered assistants  
- Workflow automation  

---

## 💡 Future Improvements

- Add database integration  
- Add authentication layer  
- Expand tools (invoice, upgrade plan, etc.)  
- Build UI dashboard  

---

## 🧪 Debug Tip

If you face errors like:
```
AttributeError: ...
```

Make sure to access tool calls correctly:

```python
result['messages'][0].tool_calls
```

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run notebook/script  
4. Test with different user inputs  
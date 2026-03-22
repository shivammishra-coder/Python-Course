# 🤖 LangChain Self-Correcting Agent (Gemini)

This project demonstrates a **self-correcting AI agent using LangChain and Google Gemini**, capable of:

- Performing mathematical calculations  
- Fetching real-world information  
- Reasoning step-by-step using tools  

The agent uses the **ReAct (Reason + Act)** framework to decide when to use tools and correct itself if needed.

---

## 🚀 Features

### ✅ Calculator Tool
Performs mathematical operations like:
- Addition
- Subtraction
- Multiplication
- Division

---

### ✅ Search Tool
Fetches factual information using Wikipedia:
- Historical data  
- People (e.g., birth year)  
- General knowledge  

---

### ✅ Self-Correcting Agent
- Uses **LangChain Agent**
- Applies **ReAct reasoning**
- Dynamically selects tools
- Handles multi-step queries

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Google Gemini (`gemini-2.5-flash`)  
- Wikipedia API  

---

## 📦 Installation

Install required dependencies:

```bash
pip install -U langchain==0.2.14 langchain-community langchain-core langchain-google-genai wikipedia
```

---

## 🔑 Setup

If using **Google Colab**, store your API key:

```python
from google.colab import userdata
GOOGLE_API_KEY = userdata.get("GOOGLE_API_KEY")
```

Or set it manually:

```bash
export GOOGLE_API_KEY=your_api_key
```

---

## ▶️ How It Works

1. User gives a query  
2. Agent decides:
   - Use **Search Tool** → to get data (e.g., Einstein birth year)  
   - Use **Calculator Tool** → to compute result  
3. Agent combines results and returns final answer  

---

## 🧪 Example

**Input:**
```
Multiply the birth year of Albert Einstein by 5.
```

**Agent Process:**
1. Searches birth year → 1879  
2. Calculates → 1879 × 5  
3. Returns result  

**Output:**
```
Final Answer: 9395
```

---

## 📂 Project Structure

```
.
├── main.ipynb / main.py   # Agent implementation
├── README.md             # Documentation
└── requirements.txt      # Dependencies
```

---

## 🧠 Concepts Covered

- ReAct Agents  
- Tool Calling in LLMs  
- Prompt-based reasoning  
- API integration  
- Self-correction in agents  

---

## ⚡ How to Run

1. Install dependencies  
2. Set your API key  
3. Run the script / notebook  
4. Modify the query to test different cases  

---

## 💡 Future Improvements

- Add more tools (weather, database, APIs)  
- Replace `eval()` with a safe math parser  
- Add UI (Streamlit / Web App)  
- Logging and monitoring  

---

## ⚠️ Note

- `eval()` is used for simplicity in the calculator tool.  
- Avoid using it in production; use safer alternatives like `numexpr` or `sympy`.  

---

## 🎯 Use Cases

- AI assistants  
- Educational tools  
- Smart calculators  
- Research assistants  
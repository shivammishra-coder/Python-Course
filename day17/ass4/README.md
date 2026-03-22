# 🧠 Grounded AI with Caching (LangChain + Gemini)

This project demonstrates a **grounded AI system with response caching**, built using:

- LangChain  
- Google Gemini (LLM)  

The system ensures:
- ✅ Answers are strictly based on provided context  
- ✅ No hallucinations (fallback response if unknown)  
- ✅ Faster responses using caching  

---

## 🚀 Features

### ✅ Strict Grounding
- AI answers ONLY from given context  
- Prevents hallucination  
- Returns fallback message if answer not found  

**Fallback Response:**
```
I do not have enough information
```

---

### ✅ Response Caching
- Stores previous queries and responses  
- Avoids repeated API calls  
- Improves performance  

---

### ✅ Gemini LLM Integration
- Uses `gemini-2.5-flash`  
- Deterministic output (`temperature=0`)  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Google Gemini  

---

## 📦 Installation

Install required dependencies:

```bash
pip install -U langchain langchain-google-genai
```

---

## 🔑 Setup

If using **Google Colab**:

```python
from google.colab import userdata
import os

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
```

Or set manually:

```bash
export GOOGLE_API_KEY=your_api_key
```

---

## ▶️ How It Works

1. User asks a question  
2. System checks:
   - If answer exists in cache → return instantly  
   - Else → send prompt to LLM  
3. LLM answers ONLY using provided context  
4. If answer not in context → returns fallback  
5. Response is stored in cache  

---

## 🧪 Scenarios Demonstrated

### 🔹 Scenario 1: First Query
- LLM generates answer from context  

**Example:**
```
Question: How many days can employees work from home?
Answer: Up to 3 days per week
```

---

### 🔹 Scenario 2: Cache Hit
- Same question asked again  
- Response returned instantly from cache  

```
Returned from Cache
```

---

### 🔹 Scenario 3: Grounding Test
- Question outside context  

**Example:**
```
Question: What is the recipe for a chocolate cake?
Answer: I do not have enough information
```

---

## 📂 Project Structure

```
.
├── main.py / notebook.ipynb   # Implementation
├── README.md                 # Documentation
└── requirements.txt          # Dependencies
```

---

## 🧠 Key Concepts

- Grounded AI  
- Prompt Engineering  
- Response Caching  
- Hallucination Prevention  
- LLM Optimization  

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run script / notebook  
4. Test with different queries  

---

## ⚙️ Customization

You can enhance this by:
- Expanding context dynamically  
- Using external documents  
- Adding persistent cache (Redis / DB)  
- Supporting multi-user sessions  

---

## ⚠️ Important Notes

- Cache is in-memory → resets on restart  
- Context is static in this example  
- Strict grounding may limit answer flexibility  

---

## 🎯 Use Cases

- Company policy assistant  
- Customer support bots  
- Knowledge-based Q&A systems  
- Safe AI applications (low hallucination risk)  

---

## 💡 Future Improvements

- Add vector database (RAG)  
- UI with Streamlit  
- Logging & monitoring  
- Multi-document support  
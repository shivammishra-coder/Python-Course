# 🧠 RAG Chunking Optimization (LangChain + FAISS + Groq)

This project demonstrates how **chunking strategies impact Retrieval-Augmented Generation (RAG)** performance.

It compares **bad vs optimized chunking configurations** to show how proper chunk size and overlap improve answer quality.

---

## 🚀 Features

### ✅ RAG Pipeline
- Document → Chunking → Embeddings → Vector Store → Retrieval → LLM  
- Built using LangChain and FAISS  

---

### ✅ Chunking Experiment
Compares two configurations:

| Configuration | Chunk Size | Overlap | Result |
|--------------|-----------|--------|--------|
| ❌ Bad        | 50        | 10     | Context loss |
| ✅ Good       | 350       | 120    | Accurate answer |

---

### ✅ HuggingFace Embeddings
- Model: `all-MiniLM-L6-v2`  
- Converts text into vectors for semantic search  

---

### ✅ Groq LLM
- Model: `llama-3.1-8b-instant`  
- Used for generating final answers  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- FAISS  
- HuggingFace Embeddings  
- Groq API  

---

## 📦 Installation

Install dependencies:

```bash
pip install -q langchain langchain-core langchain-community langchain-text-splitters langchain-huggingface langchain-groq faiss-cpu sentence-transformers
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

1. Load document (multi-section company policy)  
2. Split document into chunks  
3. Convert chunks into embeddings  
4. Store in FAISS vector database  
5. Retrieve top-k relevant chunks  
6. Pass context to LLM  
7. Generate final answer  

---

## 🧪 Experiment

### ❌ Bad Configuration
```python
chunk_size = 50
chunk_overlap = 10
```

**Problem:**
- Context gets fragmented  
- Related sections are separated  
- Model fails to connect information  

---

### ✅ Improved Configuration
```python
chunk_size = 350
chunk_overlap = 120
```

**Benefits:**
- Keeps related content together  
- Overlap preserves context across boundaries  
- Improves retrieval quality  

---

## 📊 Example Query

```
What is the deadline and budget for Project Phoenix?
```

### ❌ Bad Output:
- Incomplete / incorrect answer  

### ✅ Good Output:
```
December 31st, 2026, with a $500,000 budget.
```

---

## 🧠 Key Insight

> Small chunks break context.  
> Overlap + larger chunks preserve meaning.

---

## 📂 Project Structure

```
.
├── main.py / notebook.ipynb   # Implementation
├── README.md                 # Documentation
└── requirements.txt          # Dependencies
```

---

## 🧠 Concepts Covered

- Retrieval-Augmented Generation (RAG)  
- Chunking Strategies  
- Context Window Optimization  
- Vector Databases (FAISS)  
- Embeddings  

---

## ⚠️ Important Notes

- Too small chunk size → loss of context  
- Too large chunk size → inefficient retrieval  
- Overlap helps connect related information  

---

## ⚙️ Customization

You can experiment with:
- Different chunk sizes  
- Different overlap values  
- Different embedding models  
- Different `k` values in retrieval  

---

## 🎯 Use Cases

- Document Q&A systems  
- Enterprise knowledge search  
- Policy / legal document analysis  
- AI-powered assistants  

---

## 💡 Future Improvements

- Add visualization of chunk boundaries  
- Compare multiple embedding models  
- Add hybrid search (BM25 + vector)  
- Build UI for live experimentation  

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run script / notebook  
4. Observe output differences between configurations  
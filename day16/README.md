# 📘 LangChain + Gemini Mini Projects

This project demonstrates multiple LangChain pipelines using Google Gemini API, covering real-world use cases like:

- Data extraction from text  
- Multi-step LLM chaining  
- Document processing & embeddings  
- Retrieval-Augmented Generation (RAG)

---

## 🚀 Features / Tasks Covered

### ✅ 1. Customer Review Analyzer
Extract structured insights from unstructured product reviews.

**Input:** Raw messy review text  
**Output:**
- Sentiment (Positive / Negative)
- Core Issue summary

**Example:**
Sentiment: Negative, Core Issue: Blender lid malfunction causing mess

---

### ✅ 2. Marketing Content Generator (Chained LLM)
A multi-step pipeline that:
1. Generates a 5-word English slogan
2. Translates it into French

**Flow:**
Product Name → Slogan Generator → Translator → Final Output

---

### ✅ 3. Document Processing & Vector Store
- Creates a text file (`game_rules.txt`)
- Loads and splits documents into chunks
- Converts text into embeddings using Gemini
- Stores them in a FAISS vector database

---

### ✅ 4. Retrieval-Augmented Generation (RAG)
Implements a basic RAG pipeline:
1. Retrieve relevant chunks from vector store
2. Pass context to LLM
3. Generate accurate answers

**Example Query:**
How many points is the golden token worth?

---

## 🛠️ Tech Stack

- LangChain  
- Google Gemini (gemini-2.5-flash)  
- FAISS (Vector Store)  
- Python  

---

## 📦 Installation

```bash
pip install langchain langchain-google-genai langchain-community langchain-text-splitters faiss-cpu
```

---

## 🔑 Setup

You need a Google Gemini API Key.

Run the notebook and enter when prompted:

```
Enter your Gemini API Key:
```

Or set it manually:

```bash
export GOOGLE_API_KEY=your_api_key
```

---

## 📂 Project Structure

```
.
├── notebook.ipynb        # Main implementation
├── game_rules.txt        # Generated sample document
└── README.md             # Documentation
```

---

## 🧠 Key Concepts Demonstrated

- Prompt Engineering  
- Output Parsing  
- LLM Chaining  
- Embeddings & Vector Stores  
- Semantic Search  
- Retrieval-Augmented Generation (RAG)

---

## 🎯 Use Cases

- Customer feedback analysis  
- Marketing automation  
- Knowledge base Q&A systems  
- AI-powered document search  

---

## ⚡ How to Run

1. Open the notebook  
2. Install dependencies  
3. Enter Gemini API key  
4. Run cells sequentially  

---

## 💡 Future Improvements

- Add UI (Streamlit / React)  
- Use larger datasets  
- Improve prompt robustness  
- Add evaluation metrics  
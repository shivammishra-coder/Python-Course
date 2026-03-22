# 🧠 Metadata-Based RAG using LangChain + Gemini + Chroma

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system with **metadata filtering**, using:

- LangChain  
- Google Gemini (LLM + Embeddings)  
- Chroma Vector Database  

The system retrieves **relevant documents based on both semantic similarity and metadata (year filter)** before generating an answer.

---

## 🚀 Features

### ✅ Vector Database (Chroma)
- Stores documents with embeddings  
- Supports similarity search  

---

### ✅ Metadata Filtering
- Filters documents using metadata (e.g., year)  
- Ensures only relevant policies are retrieved  

---

### ✅ Gemini Embeddings
- Converts text into vector representations  
- Enables semantic search  

---

### ✅ Gemini LLM
- Generates answers using retrieved context  
- Ensures accurate, context-based responses  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Google Gemini (`gemini-2.5-flash`)  
- ChromaDB  

---

## 📦 Installation

Install required dependencies:

```bash
pip install -U langchain langchain-community langchain-google-genai chromadb
```

---

## 🔑 Setup

If using **Google Colab**:

```python
from google.colab import userdata
GOOGLE_API_KEY = userdata.get("GOOGLE_API_KEY")
```

Or set manually:

```bash
export GOOGLE_API_KEY=your_api_key
```

---

## ▶️ How It Works

1. Create documents with metadata:
   - Example: WFH policy for different years  

2. Convert documents into embeddings  

3. Store in Chroma vector database  

4. Retrieve documents using:
   - Semantic similarity  
   - Metadata filter (`year`)  

5. Pass retrieved context to Gemini LLM  

6. Generate final answer  

---

## 🧪 Example

### Input:
```
Query: What is the WFH policy?
Filter Year: 2024
```

### Retrieved Context:
```
Company WFH Policy: Work from home is allowed 3 days a week.
```

### Output:
```
Work from home is allowed 3 days a week.
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

- Retrieval-Augmented Generation (RAG)  
- Vector Databases  
- Metadata Filtering  
- Semantic Search  
- Embeddings  

---

## ⚡ How to Run

1. Install dependencies  
2. Set API key  
3. Run script / notebook  
4. Modify:
   - Query  
   - Metadata filter (year)  

---

## ⚙️ Customization

You can extend this by:
- Adding more metadata fields (department, region)  
- Increasing number of documents  
- Changing `k` value in similarity search  

---

## ⚠️ Important Notes

- Ensure correct metadata format:
```python
metadata={"year": 2024}
```

- If no matching metadata is found, retrieval may return empty results  

---

## 🎯 Use Cases

- Company policy assistant  
- Legal document retrieval  
- Version-controlled knowledge bases  
- Enterprise search systems  

---

## 💡 Future Improvements

- Add UI (Streamlit / Web App)  
- Store large document sets  
- Use hybrid search (keyword + semantic)  
- Add evaluation metrics for retrieval accuracy  
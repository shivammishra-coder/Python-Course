# ✂️ LangChain Text Splitter with Overlap Visualization

This project demonstrates how to use **LangChain's RecursiveCharacterTextSplitter** to:

- Split large text into smaller chunks  
- Maintain overlap between chunks  
- Visualize and verify overlapping regions  

This is especially useful for **LLM applications like RAG (Retrieval-Augmented Generation)** where context continuity is important.

---

## 🚀 Features

### ✅ Recursive Text Splitting
- Breaks long text into smaller chunks  
- Uses configurable `chunk_size`  

---

### ✅ Overlap Handling
- Maintains overlap between chunks using `chunk_overlap`  
- Ensures context is preserved across chunks  

---

### ✅ Overlap Detection
- Custom function to detect and display overlapping text  
- Helps verify correctness of chunking  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- RecursiveCharacterTextSplitter  

---

## 📦 Installation

Install dependencies:

```bash
pip install -U langchain langchain-text-splitters
```

---

## ▶️ How It Works

1. Define a large input text  
2. Configure the splitter:
   - `chunk_size = 200`
   - `chunk_overlap = 50`
3. Split text into chunks  
4. Compare adjacent chunks  
5. Detect overlapping text programmatically  

---

## 🧪 Example Output

- Displays total number of chunks  
- Prints each pair of chunks  
- Shows detected overlap between them  

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

- Text Chunking  
- Context Preservation  
- Overlapping Windows  
- Preprocessing for LLMs  

---

## ⚡ How to Run

1. Install dependencies  
2. Run the script or notebook  
3. Observe:
   - Generated chunks  
   - Overlap between chunks  

---

## ⚙️ Configuration

You can tweak:

```python
chunk_size=200
chunk_overlap=50
```

- Increase `chunk_size` → larger chunks  
- Increase `chunk_overlap` → more context retention  

---

## ⚠️ Important Note

The separator is set as:

```python
separators=[""]
```

This forces **character-level splitting**, ensuring overlap is always visible.

---

## 🎯 Use Cases

- Preparing data for LLMs  
- Building RAG pipelines  
- Document chunking for embeddings  
- Improving context retention in AI systems  

---

## 💡 Future Improvements

- Visual UI for chunk comparison  
- Support for PDF / documents  
- Integration with vector databases  
- Dynamic chunk size tuning  
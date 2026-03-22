# 🔄 Expense Approval Workflow (LangGraph + LangChain)

This project demonstrates a **workflow-based decision system** using **LangGraph**, where an expense goes through:

- Tax calculation  
- Currency conversion  
- Conditional approval routing  
- Final output generation  

It showcases how to build **stateful, multi-step AI workflows**.

---

## 🚀 Features

### ✅ Stateful Workflow
- Uses `TypedDict` to manage state across nodes  
- Tracks:
  - Original amount (USD)  
  - Tax-added amount  
  - Converted INR amount  
  - Approval decision  

---

### ✅ Multi-Step Processing

1. **Add Tax (10%)**
2. **Convert USD → INR**
3. **Route Decision Based on Amount**
4. **Approval Process**
5. **Final Output**

---

### ✅ Conditional Routing

| Amount (USD) | Decision |
|-------------|---------|
| ≤ 100       | Auto Approved |
| ≤ 1000      | Manager Approval |
| > 1000      | Finance Approval |

---

### ✅ Modular Nodes
Each step is a separate function:
- `add_tax`  
- `convert_to_inr`  
- `auto_approve`  
- `manager_approve`  
- `finance_approve`  

---

## 🛠️ Tech Stack

- Python  
- LangGraph  
- LangChain  

---

## 📦 Installation

Install required dependencies:

```bash
pip install langgraph langchain
```

---

## ▶️ How It Works

1. Input expense in USD  
2. Add 10% tax  
3. Convert amount to INR  
4. Route to appropriate approval:
   - Auto  
   - Manager  
   - Finance  
5. Print final result  

---

## 🧪 Example

### Input:
```
amount_usd = 500
```

### Flow:
```
500 USD → +10% tax → 550 USD  
550 USD → INR → 45,650 INR  
Decision → Manager Approval
```

### Output:
```
Expense in USD: 500
Amount with Tax (USD): 550
Amount in INR: 45650
Final Decision: Manager Approved
```

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

- LangGraph Workflows  
- Stateful Processing  
- Conditional Routing  
- Multi-step Pipelines  
- Decision Automation  

---

## ⚙️ Workflow Architecture

```
add_tax → convert_to_inr → decision_router
                              ↓
        ┌───────────────┬───────────────┬───────────────┐
        ↓               ↓               ↓
 auto_approve   manager_approve   finance_approve
        ↓               ↓               ↓
                final_output → END
```

---

## ⚠️ Important Notes

- Currency conversion rate is fixed (1 USD = 83 INR)  
- Tax rate is fixed at 10%  
- Workflow is synchronous and deterministic  

---

## ⚡ How to Run

1. Install dependencies  
2. Run script / notebook  
3. Modify input value:
```python
input_data = {"amount_usd": 500}
```
4. Observe workflow execution  

---

## 🎯 Use Cases

- Expense management systems  
- Approval workflows  
- Business process automation  
- Decision engines  

---

## 💡 Future Improvements

- Add real-time currency API  
- Add UI dashboard  
- Store results in database  
- Add approval notifications  
- Integrate with enterprise systems  
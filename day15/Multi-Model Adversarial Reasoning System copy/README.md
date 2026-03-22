# Multi-Model Adversarial Reasoning System

## 📌 Description

This project implements a **multi-model adversarial reasoning pipeline** using two LLMs.
It simulates a structured debate where:

* **Model A** proposes a solution
* **Model B** critiques it
* **Model A** revises its response based on critique

This approach improves reasoning quality, robustness, and logical consistency.

---

## 🚀 Features

* Multi-model orchestration (A → B → A loop)
* Structured prompt engineering
* Input validation and relevance checking
* API retry mechanism with timeout handling
* Logging of prompts and responses
* Strict JSON output formatting
* Adversarial reasoning workflow

---

## 🛠️ Technologies Used

* Python
* requests (API communication)
* logging (traceability)
* JSON (structured output)

---

## 📂 Project Structure

```
project/
│
├── main.py                      # Main application script
├── adversarial_reasoning.log    # Log file (auto-generated)
├── README.md                    # Documentation
└── requirements.txt             # Dependencies
```

---

## ⚙️ Configuration

### API Configuration

Update these values inside the script if needed:

```
BASE_API_URL = https://aimodels.jadeglobal.com:8082/ollama/api
MODEL_A_NAME = llama3.1:8b
MODEL_B_NAME = deepseek-coder:6.7b
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📥 Input

User provides a scenario/problem statement:

Example:

```
Design a scalable system for real-time fraud detection in banking.
```

---

## 🔄 Workflow

### Step 1: Model A (Initial Proposal)

* Generates structured solution
* Includes reasoning, assumptions, risks

### Step 2: Model B (Critique)

* Identifies weaknesses
* Highlights risks and edge cases
* Challenges assumptions

### Step 3: Model A (Revision)

* Improves solution based on critique
* Addresses all major concerns

---

## 📤 Output Format

The system returns structured JSON:

```
{
  "original_input": "...",
  "model_a_initial_proposal": "...",
  "model_b_critique": "...",
  "model_a_revised_response": "...",
  "final_evaluation": "..."
}
```

---

## 🧠 Key Components

### 1. InputValidator

* Validates input length
* Ensures response relevance

### 2. OllamaAPIClient

* Handles API communication
* Retry logic (3 attempts)
* Timeout management

### 3. PromptBuilder

* Constructs structured prompts
* Enables adversarial reasoning

### 4. AdversarialOrchestrator

* Controls workflow (A → B → A)
* Ensures validation at each stage

### 5. JSONFormatter

* Produces clean, valid JSON output

---

## 📊 Logging

All prompts and responses are stored in:

```
adversarial_reasoning.log
```

This helps with debugging and traceability.

---

## ⚠️ Error Handling

* Invalid input detection
* API retry mechanism
* Timeout handling
* Relevance validation
* Graceful failure messages

---

## 🏆 Key Insight

Adversarial interaction between models improves:

* Logical consistency
* Depth of reasoning
* Robustness of solutions

---

## 🚀 Future Improvements

* Add more models for multi-agent debate
* Introduce scoring/evaluation metrics
* Integrate UI dashboard
* Add streaming responses
* Implement response ranking

---

## 👨‍💻 Author

SHIVAM MISHRA

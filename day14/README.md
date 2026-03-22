# LoRA vs QLoRA Fine-Tuning (TinyLlama 1.1B)

## 📌 Description

This project demonstrates parameter-efficient fine-tuning of a 1.1B LLaMA-based model using **LoRA** and **QLoRA** techniques. It compares memory usage and performance between full precision LoRA and 4-bit quantized QLoRA.

The experiment uses the Alpaca dataset and evaluates how quantization impacts GPU memory and output quality.

---

## 🚀 Features

* Fine-tuning using LoRA (Low-Rank Adaptation)
* Quantized fine-tuning using QLoRA (4-bit)
* Memory usage comparison between LoRA and QLoRA
* Instruction-based dataset (Alpaca)
* Text generation for qualitative evaluation

---

## 🛠️ Technologies Used

* PyTorch
* Hugging Face Transformers
* Datasets (Alpaca)
* PEFT (LoRA/QLoRA)
* BitsAndBytes (4-bit quantization)
* Accelerate

---

## 📂 Project Structure

```
project/
│
├── main.py              # Training + evaluation script
├── README.md            # Documentation
├── requirements.txt     # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd project
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python main.py
```

---

## 📊 Model Used

* **TinyLlama-1.1B-Chat**
* Lightweight LLaMA-based instruction model

---

## 📥 Dataset

* Alpaca Dataset (subset of 2000 samples)
* Instruction-based format:

  * Instruction
  * Input
  * Output

---

## 🔄 Workflow

### 1. Tokenization

* Combines instruction + input + output
* Converts text into token IDs
* Uses max length = 256

### 2. LoRA Fine-Tuning

* Model loaded in FP16
* LoRA applied on:

  * `q_proj`
  * `v_proj`
* Trains only a small number of parameters

### 3. QLoRA Fine-Tuning

* Model loaded in 4-bit quantization (NF4)
* Same LoRA configuration applied
* Reduces model precision for efficiency

---

## 🧪 Evaluation

* Generates outputs for test prompts:

  * Machine learning explanation
  * Motivational paragraph
  * Benefits of exercise

---

## 📈 Results

| Method | Peak GPU Memory |
| ------ | --------------- |
| LoRA   | 4.18 GB         |
| QLoRA  | 5.75 GB         |

---

## 🧠 Key Insight

Although QLoRA is designed to reduce memory usage, in this experiment:

* The model (1.1B) was already small
* Quantization overhead increased memory usage slightly

👉 Conclusion:
**QLoRA is more beneficial for larger models (7B, 13B, etc.)**

---

## ⚠️ Requirements

* GPU with CUDA support
* Minimum 6GB VRAM recommended
* Python 3.8+

---

## 🏆 Future Improvements

* Test on larger models (7B+)
* Add evaluation metrics (BLEU, ROUGE)
* Save and reload trained adapters
* Add inference benchmarking

---

## 👨‍💻 Author

SHIVAM MISHRA

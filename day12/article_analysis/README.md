# LLM Article Summarizer

## 📌 Description

This project is a Python-based application that connects to a Large Language Model (LLM) API to generate structured summaries from input text. The system builds a prompt, sends it to the LLM, and retrieves a JSON response containing key insights such as summary, important points, themes, and target audience.

---

## 🚀 Features

* API connectivity check before execution
* Dynamic prompt generation
* Structured JSON output from LLM
* Environment variable configuration using `.env`
* Robust error handling (timeout, connection issues, API errors)
* Modular and scalable code design

---

## 🛠️ Technologies Used

* Python
* requests (for API communication)
* python-dotenv (for environment variable management)
* jsonschema (for future JSON validation)

---

## 📂 Project Structure

```
project/
│
├── main.py              # Main script
├── .env                 # Environment variables
├── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repository-link>
cd project
```

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and add:

```
LLM_BASE_URL=http://your-api-url
LLM_MODEL=your-model-name
LLM_VERIFY_SSL=False
LLM_TIMEOUT=120
```

---

## ▶️ How to Run

```
python main.py
```

---

## 📥 Input

The program currently uses a sample article defined inside the script:

```
Artificial intelligence is transforming industries by automating tasks,
improving decision-making, and enabling predictive analytics.
```

---

## 📤 Output

The LLM returns structured JSON in the following format:

```
{
  "summary": "Short summary of the article",
  "important_points": ["Point 1", "Point 2"],
  "key_themes": ["Theme 1", "Theme 2"],
  "target_audience": "Intended audience"
}
```

---

## ⚠️ Error Handling

* Stops execution if API is not reachable
* Handles API timeout errors
* Handles connection failures
* Displays meaningful error messages

---

## 🧠 Design Approach

* Modular design separating API calls, prompt creation, and execution
* Environment-based configuration for flexibility
* Scalable structure for future NLP enhancements

---

## 🏆 Future Improvements

* Implement JSON schema validation using `jsonschema`
* Accept input from files instead of hardcoded text
* Add logging system for better debugging
* Build a user interface (CLI or Web UI)
* Add support for multiple LLM providers

---

## 👨‍💻 Author

SHIVAM MISHRA

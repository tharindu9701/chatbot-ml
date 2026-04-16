# 🤖 AI Customer Support Chatbot

A simple and efficient AI-powered chatbot that answers customer questions using your business FAQ data.

---

## 🚀 Overview

This project is a **CSV-based AI chatbot** designed to automate customer support.  
It uses machine learning (TF-IDF + cosine similarity) to match user queries with the most relevant answers.

✔ No API required  
✔ No monthly cost  
✔ Fast and lightweight  

---

## 💡 Features

- 📂 Upload your own FAQ CSV file  
- ⚡ Instant responses to user questions  
- 🧠 Machine learning-based matching  
- 💻 Clean and simple web interface (Streamlit)  
- 🔓 Full source code included  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 📁 Project Structure

chatbot-ml/
│
├── app/
│   ├── app.py
│   └── chatbot.py
│
├── data/
│   └── faq.csv
│
├── model/
│   ├── vectorizer.pkl
│   └── question_vectors.pkl
│
├── docs/
│   └── AI_Chatbot_Documentation.pdf
│
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. Upload a CSV file with:
   - `question`
   - `answer`

2. The system:
   - Converts text into vectors  
   - Compares similarity  

3. The chatbot:
   - Finds best match  
   - Returns the correct answer  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py

⚠️ Limitations
	•	Works best with structured FAQ data
	•	Not suitable for complex conversations
	•	Accuracy depends on dataset quality

⸻

🔮 Future Improvements
	•	GPT / LLM integration
	•	Multi-language support
	•	Database integration
	•	Voice input

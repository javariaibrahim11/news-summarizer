# news-summarizer
AI-powered News Summarizer using BART Transformer model and Gradio UI.
# 📰 AI News Summarizer  
A simple and powerful **AI-based News Summarizer Web App** built using **Python, Hugging Face Transformers, and Gradio**.  
This app converts long news articles into short, clear summaries.

---

## 🚀 Live Demo  
👉 https://huggingface.co/spaces/javaria-ibrahim/news-summarizer  

---

## 🧠 Model  
This app uses the Hugging Face summarization model:

- **facebook/bart-large-cnn**

Great for summarizing long news and articles.

---

## 🎨 Features  
- Summarizes long news instantly  
- Clean and simple Gradio UI  
- Accurate BART summarizer  
- Easy to use  
- Fully deployed on Hugging Face  

---

## 📂 Project Structure  

news-summarizer/  
│  
├── app.py               # Main application code (Gradio UI + summarizer)  
├── requirements.txt     # Dependencies (Transformers + Gradio)  
└── README.md            # Project documentation  

---

## ▶️ Run Locally  

1️⃣ Clone the repository  
git clone https://github.com/javariaibrahim11/news-summarizer  

2️⃣ Install dependencies  
pip install -r requirements.txt  

3️⃣ Run the app  
python app.py  

App will open here:  
http://localhost:7860 🚀  

---

## ✨ How It Works  
1. User pastes a long news article  
2. BART model processes the text  
3. Generates a short summary  
4. Summary appears on Gradio UI  
5. User can clear and add new article anytime  

---

## 🛠️ Main Code Snippet  

def summarize_news(text):  
    summary = summarizer(text, max_length=60, min_length=10, do_sample=False)  
    return summary[0]["summary_text"]  

---

## 📌 Future Improvements  
- Add multiple models  
- Add PDF/Text upload  
- Add summary length control  
- Improve UI  
- Add key-points extraction  

---

## 👩‍💻 Author  
**Javaria Ibrahim**  

GitHub: https://github.com/javariaibrahim11  
Hugging Face: https://huggingface.co/javaria-ibrahim  

---

## 📜 License  
This project is licensed under the **MIT License**.

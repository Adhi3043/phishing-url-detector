# 🔐 AI-Powered Real-Time Phishing URL Detector

This is a web-based phishing URL detection app that uses **machine learning (TF-IDF + Random Forest)** to classify links as legitimate or phishing in real time.

## 🚀 Features

- Real-time phishing detection via Flask web interface
- AI model trained on URL structure patterns (TF-IDF)
- Clean and modern UI (HTML + CSS)
- Lightweight and fast
- Easy to test, use, and deploy

## 🧠 Tech Stack

- Python
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- HTML/CSS (with custom styling)

## 💻 How to Run Locally

```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd app
python app.py

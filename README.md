# 🔐 Real-Time Phishing URL Detector

A machine learning-powered web application that detects phishing URLs in real-time using a Random Forest classifier and TF-IDF vectorization.

---

## 🚀 Features

- ✅ Real-time phishing detection
- ⚙️ Machine Learning backend (TF-IDF + Random Forest)
- 💻 Flask web application
- 🎨 Clean UI with HTML & CSS
- 🔐 SSH-integrated secure GitHub deployment
- 🧠 Built and tested on Kali Linux

---

## 🧠 How It Works

1. **TF-IDF Vectorization** – URLs are transformed into numerical vectors.
2. **Random Forest Classifier** – Predicts if the URL is `phishing ❌` or `legitimate ✅`.
3. **Flask Web App** – Enter a URL and get instant results in your browser.

---

## 🗂 Project Structure


---

## 🔧 Setup & Run

```bash
# Clone the repo
git clone git@github.com:Adhi3043/phishing-url-detector.git
cd phishing-url-detector

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt

# Run the app
cd app
python app.py


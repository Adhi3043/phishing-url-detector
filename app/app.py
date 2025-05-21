from flask import Flask, request, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = pickle.load(open("model_tfidf.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        vectorized = vectorizer.transform([url])
        prediction = model.predict(vectorized)[0]
        result = "Phishing ❌" if prediction == 1 else "Legitimate ✅"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


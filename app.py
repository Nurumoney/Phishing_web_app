import joblib
import re
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model = joblib.load("phishing_model.pkl")

# Feature extraction function
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        int('https' in url),
        int('@' in url),
        int('-' in url),
        int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        url.count('/'),
        int(any(word in url for word in ['verify', 'account', 'login', 'secure', 'update', 'check']))
    ]

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict([features])[0]
    return render_template("index.html", prediction=prediction)

# Note: Do not include app.run() — Gunicorn will handle it on Render

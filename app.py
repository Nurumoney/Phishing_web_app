import joblib
from flask import Flask
app = Flask(__name__), request, render_template
import re

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

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

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict([features])[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

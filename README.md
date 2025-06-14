# 🔐 Ellams AI Phishing Scanner_web_app

A lightweight AI-powered web app that detects phishing URLs in real-time using a trained machine learning model.

---

## 🚨 Problem

Phishing websites are used to steal sensitive information by tricking users into thinking they’re on a legitimate site. Traditional methods often fail to catch them early.

---

## 💡 Solution

Ellams Phishing Scanner uses machine learning to analyze URL characteristics and predict whether a link is suspicious or safe. It’s fast, simple, and privacy-friendly — no data is stored.

---

## ⚙️ How It Works

- Extracts features like URL length, use of symbols (`@`, `-`), presence of keywords like `login`, `verify`, and others.
- Trained on real phishing and legitimate URLs.
- Predicts using a Random Forest Classifier.

---

## 🧠 Tech Stack

- Python (Flask)
- Scikit-learn
- HTML (Jinja2 Templates)
- Joblib (for model persistence)

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/ellams_phishing_scan.git
cd ellams_phishing_scan

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

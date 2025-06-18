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


```

### 🌐 Live Demo
‎
‎Access the deployed app here:  
‎🔗 [https://phishing-web-app-qs2z.onrender.com](https://phishing-web-app-qs2z.onrender.com)
‎

‎### 🚀 How to Use
‎
‎1. Open the link above in your browser.
‎2. Enter a URL you want to check (e.g., `http://example.com`).
‎3. Click **"Check URL"**.
‎4. You'll see whether the URL is **Phishing** or **Legitimate**.
‎
‎⚠️ *Note:* On Render's free tier, the app might take ~30 seconds to wake up if it has been idle.
‎
‎---
‎
‎### 🧠 AI in Action
‎
‎- The model was trained using a dataset of phishing and legitimate URLs.
‎- A `.pkl` file (`phishing_model.pkl`) is used to make real-time predictions.
‎- The ML pipeline was created using Python’s `scikit-learn`.
‎
‎---
‎
‎### 🛠️ Technologies Used
‎
‎- Python
‎- Flask
‎- Scikit-learn
‎- HTML/CSS (basic UI)
‎- Hosted on Render
‎
‎---
‎
‎### 📁 Project Structure


Phishing_web_app/
├── app.py                 # Flask web server
├── phishing_model.pkl     # Trained ML model
├── requirements.txt       # Python dependencies
├── train_model.py         # Script to train the model
├── phishing_site_urls.csv # Dataset for training (optional)
├── templates/
│   └── index.html         # HTML frontend form
└── README.md              # Project documentation


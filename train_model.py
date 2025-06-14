import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset (CSV with 'url' and 'label' columns)
data = pd.read_csv("phishing_site_urls.csv")

# Feature extraction function
def extract_features(url):
    return {
        "url_length": len(url),
        "has_at_symbol": int("@" in url),
        "has_hyphen": int("-" in url),
        "has_https": int("https" in url),
        "has_ip": int(any(char.isdigit() for char in url.split("/")[2])) if url.startswith("http") else 0,
        "count_dots": url.count("."),
        "has_suspicious_words": int(any(word in url.lower() for word in ["login", "verify", "update", "secure"]))
    }

# Convert to feature DataFrame
features = data["url"].apply(extract_features).apply(pd.Series)
labels = data["label"]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("✅ Model trained and saved as phishing_model.pkl")

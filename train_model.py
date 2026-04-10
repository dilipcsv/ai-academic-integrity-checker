import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
with open("data/data_human.txt", "r", encoding="utf-8") as f:
    human = f.readlines()

with open("data/data_ai.txt", "r", encoding="utf-8") as f:
    ai = f.readlines()

# Combine data
texts = human + ai
labels = [0]*len(human) + [1]*len(ai)   # 0 = human, 1 = AI

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Model
model = LogisticRegression()
model.fit(X, labels)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")
import pandas as pd
import string
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

nltk.download('stopwords')
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english')) 

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake['label'] = 0
true['label'] = 1

data = pd.concat([fake, true])
data = data.sample(frac=1).reset_index(drop=True)


def clean_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return " ".join(words)


X = data['text']
y = data['label']

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

with open("fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and Vectorizer saved successfully!")



y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


def predict_news(news):
    news = clean_text(news)
    news_vec = vectorizer.transform([news])
    return "Real News" if model.predict(news_vec)[0] == 1 else "Fake News"

print(predict_news("Breaking news: Government launches new policy"))

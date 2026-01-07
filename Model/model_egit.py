
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# VERİ SETİ
df = pd.read_csv('mesajlar.csv')



vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']


clf = MultinomialNB()
clf.fit(X, y)


joblib.dump(clf, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model başarıyla eğitildi ve kaydedildi!")
print("Dosyalar: spam_model.pkl, vectorizer.pkl")
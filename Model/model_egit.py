# Dosya: model_egit.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# 1. VERİ SETİ (Gerçek hayatta burası binlerce satır olur, şimdilik demo verisi)
data = {
    'text': [
        "Hesabınız bloke oldu hemen tıklayın",  # Phishing
        "Tebrikler iphone kazandınız linke git", # Phishing
        "Şifrenizi güncellemek için buraya basın", # Phishing
        "Acil para gönder banka hesabım değişti", # Phishing
        "Faturanızın son ödeme tarihi geçti",    # Phishing
        "Merhaba nasılsın yarın buluşalım mı",   # Güvenli
        "Toplantı notlarını ekte gönderiyorum",  # Güvenli
        "Akşam yemeği için rezervasyon yaptım",  # Güvenli
        "Proje dosyalarını drive'a yükledim",    # Güvenli
        "Bugün hava çok güzel değil mi"          # Güvenli
    ],
    'label': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # 1: Phishing, 0: Güvenli
}

df = pd.DataFrame(data)

# 2. VEKTÖRLEŞTİRME (Metni sayılara çevirme)
# Makine kelimeleri anlamaz, sayıları anlar.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. MODEL EĞİTİMİ (Naive Bayes Algoritması)
clf = MultinomialNB()
clf.fit(X, y)

# 4. MODELİ VE VEKTÖRLEYİCİYİ KAYDETME
# C# tarafında tekrar eğitim yapmamak için beyni dondurup saklıyoruz.
joblib.dump(clf, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model başarıyla eğitildi ve kaydedildi!")
print("Dosyalar: spam_model.pkl, vectorizer.pkl")
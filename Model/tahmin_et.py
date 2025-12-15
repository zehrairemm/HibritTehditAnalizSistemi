import sys
import joblib
import os

# Model dosyalarının olduğu yolu bul (Bu dosyanın olduğu yer)
current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    # Modelleri yükle
    clf = joblib.load(os.path.join(current_dir, 'spam_model.pkl'))
    vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))

    # C#'tan gelen metni al
    if len(sys.argv) > 1:
        gelen_metin = sys.argv[1]
    else:
        gelen_metin = "Test verisi yok"

    # Tahmin et
    vektor = vectorizer.transform([gelen_metin])
    tahmin = clf.predict(vektor)[0]
    olasilik = clf.predict_proba(vektor).max() * 100

    # Sonucu yazdır
    if tahmin == 1:
        print(f"TEHLIKELI|%{olasilik:.2f}")
    else:
        print(f"GUVENLI|%{olasilik:.2f}")

except Exception as e:
    # Hata olursa açıkça yazsın
    print(f"PYTHON_HATASI|{str(e)}")
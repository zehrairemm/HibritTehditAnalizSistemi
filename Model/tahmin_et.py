import sys
import joblib
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

try:
   
    clf = joblib.load(os.path.join(current_dir, 'spam_model.pkl'))
    vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))

   
    if len(sys.argv) > 1:
        gelen_metin = sys.argv[1]
    else:
        gelen_metin = "Test verisi yok"

    
    vektor = vectorizer.transform([gelen_metin])
    tahmin = clf.predict(vektor)[0]
    olasilik = clf.predict_proba(vektor).max() * 100

   
    if tahmin == 1:
        print(f"TEHLIKELI|%{olasilik:.2f}")
    else:
        print(f"GUVENLI|%{olasilik:.2f}")

except Exception as e:
    # Hata mesajı
    print(f"PYTHON_HATASI|{str(e)}")
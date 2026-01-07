#  Hibrit Tehdit Analiz Sistemi (C# & Python)

Bu proje, metin tabanlı mesajları (SMS, E-posta vb.) analiz ederek **Phishing (Oltalama)** saldırılarını tespit eden hibrit bir siber güvenlik uygulamasıdır.  
Kullanıcı arayüzü ve sistem yönetimi için **C#**, makine öğrenmesi ve veri işleme süreçleri için **Python** kullanılmıştır.

---

##  Özellikler
- **NLP Tabanlı Sınıflandırma:** Doğal Dil İşleme teknikleri kullanılarak metinler analiz edilir.
- **Hibrit Mimari:** C# uygulaması, Python scriptlerini arka planda bir süreç (Process) olarak çalıştırır ve sonuçları dinamik olarak yorumlar.
- **Makine Öğrenmesi:** Multinomial Naive Bayes algoritması ile phishing tespiti yapılır.

---

##  Kullanılan Teknolojiler

**Programlama Dilleri**
- C#
- Python

**Python Kütüphaneleri**
- Pandas (veri işleme)
- Scikit-learn (model eğitimi ve vektörleştirme)
- Joblib (model kaydetme / yükleme)

**Platform**
- .NET CLI (Console Application)

---

##  Dosya Yapısı
- `Program.cs` → Kullanıcı girdisini alan ve Python modelini tetikleyen C# ana dosyası  
- `Model/model_egit.py` → CSV veri seti üzerinden makine öğrenmesi modelini eğiten Python betiği  
- `Model/tahmin_et.py` → Gelen metni analiz ederek sonucu döndüren Python betiği  
- `Model/mesajlar.csv` → Modelin eğitiminde kullanılan veri seti  

---

##  Kurulum ve Çalıştırma

### 1 Python Bağımlılıklarını kurun
```bash
pip install pandas scikit-learn joblib

### 2 Modeli Eğitin
python model_egit.py

###   C# uygulamasını çalıştırın 

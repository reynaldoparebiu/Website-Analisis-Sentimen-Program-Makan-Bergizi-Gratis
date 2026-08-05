# MBG Insight — Website Informasi & Analisis Sentimen Program MBG

Aplikasi Streamlit 2 halaman:

1. **Beranda** (`app.py`) — informasi lengkap tentang Program Makan Bergizi
   Gratis (MBG): apa itu, alur Yayasan → Dapur → Sekolah, urgensi, dan
   sasaran program, dengan ilustrasi orisinal bertema baki makan.
2. **Analisis Sentimen** (`pages/1_Analisis_Sentimen.py`) — alat uji model
   klasifikasi sentimen (Multinomial Naive Bayes + TF-IDF) untuk kalimat
   opini publik tentang MBG, mendukung input satu kalimat maupun unggah
   CSV massal.

## Struktur folder

```
mbg_app/
├── app.py
├── pages/
│   └── 1_Analisis_Sentimen.py
├── utils/
│   ├── preprocessing.py
│   └── theme.py
├── models/
│   ├── model_naive_bayes_final.pkl
│   └── tfidf_vectorizer_final.pkl
├── images/
│   ├── Dapur.jpeg
│   ├── Makan_mbg.jpg
│   └── pengantaran.jpeg
├── .streamlit/
│   └── config.toml
└── requirements.txt
```

## Menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Community Cloud

1. Push folder ini (termasuk isi `models/`) ke sebuah repo GitHub.
2. Buka [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Pilih repo tersebut, isi:
   - **Main file path**: `app.py`
4. Klik **Deploy**. Halaman kedua akan otomatis muncul di sidebar karena
   berada di folder `pages/`.

> File `.pkl` di `models/` berukuran kecil (±140 KB & ±115 KB) sehingga
> aman disertakan langsung di repo GitHub.


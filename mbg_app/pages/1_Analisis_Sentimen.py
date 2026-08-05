import pickle
import warnings
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.preprocessing import clean_text
from utils.theme import BASE_CSS, PINE, MANGO, SAGE, CLAY

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Analisis Sentimen • MBG",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(BASE_CSS, unsafe_allow_html=True)

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
COLOR_MAP = {"Positif": SAGE, "Netral": MANGO, "Negatif": CLAY}


JUDUL_PENELITIAN = (
    "Analisis Sentimen Masyarakat terhadap Program Makan Bergizi Gratis (MBG) "
    "Pada Media Sosial X Menggunakan Metode Multinomial Naive Bayes"
)


with st.sidebar:
    st.markdown("### 🍚 MBG Insight")
    st.markdown("Ruang informasi & riset seputar Program Makan Bergizi Gratis.")
    st.markdown("---")
    st.markdown("**Halaman**")
    st.page_link("app.py", label="Beranda · Tentang MBG", icon="🏠")
    st.page_link(
        "pages/1_Analisis_Sentimen.py",
        label="Analisis Sentimen",
        icon="🔎",
    )
    st.markdown("---")
    st.caption("Model: Multinomial Naive Bayes + TF-IDF")


@st.cache_resource(show_spinner=False)
def load_artifacts():
    with open(MODEL_DIR / "model_naive_bayes_Terbaru.pkl", "rb") as f:
        model = pickle.load(f)
    with open(MODEL_DIR / "tfidf_vectorizer_Terbaru.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


def predict(texts, model, vectorizer):
    cleaned = [clean_text(t) for t in texts]
    X = vectorizer.transform(cleaned)
    preds = model.predict(X)
    probas = model.predict_proba(X)
    return cleaned, preds, probas


def proba_chart(labels, values):
    order = ["Positif", "Netral", "Negatif"]
    ordered = [(lab, val) for lab in order for l2, val in zip(labels, values) if l2 == lab]
    labs = [o[0] for o in ordered]
    vals = [o[1] for o in ordered]
    colors = [COLOR_MAP[l] for l in labs]

    fig = go.Figure(
        go.Bar(
            x=vals,
            y=labs,
            orientation="h",
            marker_color=colors,
            text=[f"{v*100:.1f}%" for v in vals],
            textposition="outside",
            cliponaxis=False,
        )
    )
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=30, t=10, b=10),
        xaxis=dict(range=[0, 1], tickformat=".0%", showgrid=False),
        yaxis=dict(showgrid=False),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#22291F"),
    )
    return fig


# Header
st.markdown(
    f"""
    <div class="mbg-hero">
        <span class="mbg-eyebrow">Model Klasifikasi Teks</span>
        <h1 style="font-size:2rem;">Analisis Sentimen Masyarakat terhadap Program Makan Bergizi Gratis (MBG)</h1>
        <p>{JUDUL_PENELITIAN}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

try:
    model, vectorizer = load_artifacts()
    model_ready = True
except Exception as e:
    model_ready = False
    st.error(
        "Model belum dapat dimuat. Pastikan file `model_naive_bayes_final.pkl` "
        "dan `tfidf_vectorizer_final.pkl` ada di folder `models/`.\n\n"
        f"Detail: {e}"
    )

# Info model
if model_ready:
    m1, m2, m3, m4 = st.columns(4)
    info = [
        ("Algoritma", "Multinomial Naive Bayes"),
        ("Metode Ekstraksi Fitur", "TF-IDF (Unigram + Bigram)"),
        ("Penyeimbangan DataLatih", "SMOTE"),
        ("3 Kelas Sentimen", "Positif · Netral · Negatif"),
    ]
    for col, (label, val) in zip([m1, m2, m3, m4], info):
        with col:
            st.markdown(
                f"""<div class="stat-box">
                        <div class="stat-num" style="font-size:1.05rem;">{val}</div>
                        <div class="stat-label">{label}</div>
                    </div>""",
                unsafe_allow_html=True,
            )

st.markdown('<hr class="divider-thin"/>', unsafe_allow_html=True)

tab_single, tab_about = st.tabs(
    ["✍️ Uji Satu Kalimat", "ℹ️ Tentang Model"]
)


# Tab 1 — single sentence
with tab_single:
    st.markdown('<p class="section-eyebrow">Coba Sendiri</p>', unsafe_allow_html=True)
    st.markdown("### Masukkan kalimat atau opini tentang MBG")

    example = st.selectbox(
        "Atau pilih contoh cepat",
        [
            "— pilih contoh —",
            "Program makan bergizi gratis ini sangat membantu anak-anak sekolah, terima kasih pemerintah.",
            "MBG ini cuma buang-buang anggaran negara, ga jelas manfaatnya buat siswa.",
            "mbg my bini gweh.",
        ],
    )
    default_text = "" if example == "— pilih contoh —" else example

    user_text = st.text_area(
        "Kalimat",
        value=default_text,
        height=120,
        placeholder="Contoh: Sejak ada MBG, anak saya jadi lebih semangat berangkat sekolah...",
        label_visibility="collapsed",
    )

    predict_clicked = st.button("Analisis Sentimen", type="primary", disabled=not model_ready)

    if predict_clicked:
        if not user_text.strip():
            st.warning("Silakan masukkan kalimat terlebih dahulu.")
        else:
            cleaned, preds, probas = predict([user_text], model, vectorizer)
            label = preds[0]
            proba_row = probas[0]

            badge_class = {
                "Positif": "badge-positif",
                "Netral": "badge-netral",
                "Negatif": "badge-negatif",
            }[label]

            r1, r2 = st.columns([1, 1.4], gap="large")
            with r1:
                st.markdown('<p class="section-eyebrow">Hasil Prediksi</p>', unsafe_allow_html=True)
                st.markdown(
                    f'<span class="badge {badge_class}">{label}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"<p style='margin-top:0.8rem;color:#5B6459;'>Keyakinan tertinggi: "
                    f"<b>{max(proba_row)*100:.1f}%</b></p>",
                    unsafe_allow_html=True,
                )
                with st.expander("Lihat teks setelah pra-pemrosesan"):
                    st.code(cleaned[0] or "(kosong setelah dibersihkan)")
            with r2:
                st.markdown('<p class="section-eyebrow">Distribusi Probabilitas</p>', unsafe_allow_html=True)
                st.plotly_chart(
                    proba_chart(list(model.classes_), list(proba_row)),
                    use_container_width=True,
                    config={"displayModeBar": False},
                )


# Tab 2 — about model
with tab_about:
    st.markdown('<p class="section-eyebrow">Metodologi</p>', unsafe_allow_html=True)
    st.markdown("### Bagaimana Model Ini Bekerja")
    st.markdown(
        """
Model ini mengklasifikasikan sebuah opini masyarakat terhadap **Program Makan Bergizi Gratis (MBG)**
ke dalam tiga kelas sentimen (**Positif**, **Netral**, dan **Negatif** menggunakan algoritma 
Multinomial Naive Bayes dengan representasi fitur Term Frequency–Inverse Document Frequency (TF-IDF).

1. **Pra-pemrosesan teks** : Data teks diproses melalui tahapan cleaning, case folding, 
   normalisasi, tokenisasi, penghapusan stopword, dan stemming untuk menghasilkan teks 
   yang bersih dan konsisten.
2. **Ekstraksi fitur TF-IDF** : Teks hasil pra-pemrosesan diubah menjadi representasi numerik menggunakan 
   **TF-IDF (Unigram & Bigram)** sehingga setiap dokumen dapat diproses oleh model klasifikasi.
3. **Klasifikasi Multinomial Naive Bayes** Data latih diseimbangkan menggunakan **SMOTE**, kemudian model 
   **Multinomial Naive Bayes** digunakan untuk mengklasifikasikan opini ke dalam kategori **Positif, Netral, atau Negatif**.

*Catatan: Model dikembangkan menggunakan data opini masyarakat dari media sosial X yang telah melalui tahapan 
pra-pemrosesan, ekstraksi fitur TF-IDF, dan pelatihan model sebelum digunakan untuk melakukan prediksi sentimen.*
        """
    )

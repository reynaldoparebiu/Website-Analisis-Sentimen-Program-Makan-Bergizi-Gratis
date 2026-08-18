from pathlib import Path

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from utils.theme import BASE_CSS, PINE, MANGO, SAGE, CLAY


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="MBG • Makan Bergizi Gratis",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PATH APLIKASI
# ============================================================

APP_DIR = Path(__file__).resolve().parent
IMAGE_DIR = APP_DIR / "images"


# ============================================================
# CSS UTAMA
# ============================================================

# CSS dari theme.py
st.markdown(BASE_CSS, unsafe_allow_html=True)

# CSS tambahan khusus halaman Beranda
st.markdown(
    """
<style>

/* =========================================================
   PENGATURAN GAMBAR UMUM
   Membatasi ukuran di layar besar agar tidak over-scale
   ========================================================= */

/* Pusatkan gambar jika ukurannya lebih kecil dari lebar kolom */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}

[data-testid="stImage"] img {
    max-width: 100%;
    height: auto;
    max-height: 450px; /* Batas tinggi maksimal untuk layar besar, bisa disesuaikan (misal: 400px - 500px) */
    object-fit: contain; /* Memastikan gambar tetap proporsional dan tidak terpotong */
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}


/* =========================================================
   HERO SLIDER
   ========================================================= */

.menu-slider-container {
    width: 100%;
    margin-top: 0;
}

.menu-slider-container img {
    width: 100%;
    height: auto;
    max-height: 360px;
    object-fit: contain;
    border-radius: 18px;
}


/* =========================================================
   JUDUL FOTO MENU
   ========================================================= */

.menu-title {
    text-align: center;
    color: #214332;
    font-weight: 700;
    font-size: 15px;
    margin-top: 10px;
}


/* =========================================================
   INDIKATOR SLIDER
   ========================================================= */

.menu-indicator {
    text-align: center;
    color: #214332;
    font-size: 16px;
    letter-spacing: 4px;
    margin-top: 4px;
}


/* =========================================================
   JUDUL TAHAPAN
   ========================================================= */

.alur-title {
    color: #214332;
    font-weight: 700;
    font-size: 18px;
    margin-top: 15px;
    margin-bottom: 5px;
}


/* =========================================================
   RESPONSIVE MOBILE
   ========================================================= */

@media (max-width: 768px) {

    .menu-title {
        font-size: 14px;
    }

    .menu-indicator {
        font-size: 15px;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("### 🍚 MBG Insight")

    st.markdown(
        "Ruang informasi & riset seputar Program Makan Bergizi Gratis."
    )

    st.markdown("---")

    st.markdown("**Halaman**")

    st.page_link(
        "app.py",
        label="Beranda · Tentang MBG",
        icon="🏠",
    )

    st.page_link(
        "pages/1_Analisis_Sentimen.py",
        label="Analisis Sentimen",
        icon="🔎",
    )

    st.markdown("---")

    st.caption("Dibangun dengan Streamlit")


# ============================================================
# DATA FOTO MENU
# ============================================================

menu_images = [
    IMAGE_DIR / "menu1.jpeg",
    IMAGE_DIR / "menu2.jpeg",
    IMAGE_DIR / "menu3.jpeg",
]

menu_titles = [
    "Menu Makan Bergizi Gratis 1",
    "Menu Makan Bergizi Gratis 2",
    "Menu Makan Bergizi Gratis 3",
]


# ============================================================
# VALIDASI FILE GAMBAR
# ============================================================

for image_path in menu_images:
    if not image_path.exists():
        st.error(
            f"❌ File gambar tidak ditemukan: {image_path.name}"
        )
        st.info(
            "Pastikan file gambar berada di folder: mbg_app/images/"
        )
        st.stop()


# ============================================================
# AUTO SLIDE
# BERGANTI SETIAP 4 DETIK
# ============================================================

slide_count = st_autorefresh(
    interval=4000,
    limit=None,
    key="auto_menu_slider",
)

current_index = slide_count % len(menu_images)


# ============================================================
# HERO SECTION
# ============================================================

hero_col, illus_col = st.columns(
    [1.55, 1],
    gap="large",
)


# ============================================================
# HERO KIRI
# DIPERTAHANKAN SEPERTI DESAIN SEBELUMNYA
# ============================================================

with hero_col:

    hero_html = """
<div class="mbg-hero">
<span class="mbg-eyebrow">Program Strategis Nasional</span>
<h1>Apa itu Makan Bergizi Gratis (MBG)?</h1>
<p>
Program Makan Bergizi Gratis (MBG) adalah salah satu program strategis nasional yang
diselenggarakan oleh pemerintah melalui Badan Gizi Nasional (BGN) untuk menyediakan
makanan bergizi kepada peserta didik, ibu hamil, ibu menyusui, dan balita. Program ini
bertujuan meningkatkan kualitas gizi masyarakat, mendukung tumbuh kembang anak,
mempercepat penurunan prevalensi stunting, serta mewujudkan sumber daya manusia
Indonesia yang sehat, cerdas, dan produktif.
</p>
</div>
"""

    st.markdown(
        hero_html,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO KANAN
# SLIDER FOTO MENU
# ============================================================

with illus_col:

    # Menampilkan gambar secara utuh
    st.image(
        str(menu_images[current_index]),
        use_container_width=True,
    )

    # Judul gambar
    title_html = (
        f'<div class="menu-title">'
        f'{menu_titles[current_index]}'
        f'</div>'
    )

    st.markdown(
        title_html,
        unsafe_allow_html=True,
    )

    # Indikator ● ○ ○
    indicators = " ".join(
        "●" if i == current_index else "○"
        for i in range(len(menu_images))
    )

    indicator_html = (
        f'<div class="menu-indicator">'
        f'{indicators}'
        f'</div>'
    )

    st.markdown(
        indicator_html,
        unsafe_allow_html=True,
    )


# ============================================================
# STATISTIK RINGKAS
# ============================================================

st.markdown(
    '<p class="section-eyebrow">SEKILAS ANGKA</p>',
    unsafe_allow_html=True,
)

s1, s2, s3, s4 = st.columns(4)

stats = [
    (
        "82,9 juta",
        "Target penerima manfaat nasional",
    ),
    (
        "32.000",
        "Target Satuan Pelayanan Pemenuhan Gizi (SPPG)",
    ),
    (
        "2,4 Juta",
        "Ibu hamil, ibu menyusui, dan balita",
    ),
    (
        "18% → 14%",
        "Target prevalensi stunting tahun 2029",
    ),
]

for col, (num, label) in zip(
    [s1, s2, s3, s4],
    stats,
):

    with col:

        stat_html = (
            '<div class="stat-box">'
            f'<div class="stat-num">{num}</div>'
            f'<div class="stat-label">{label}</div>'
            '</div>'
        )

        st.markdown(
            stat_html,
            unsafe_allow_html=True,
        )


st.caption("*Data berdasarkan target resmi pemerintah.")


# ============================================================
# GARIS PEMBATAS
# ============================================================

st.markdown(
    '<hr class="divider-thin"/>',
    unsafe_allow_html=True,
)


# ============================================================
# ALUR PROGRAM
# ============================================================

st.markdown(
    '<p class="section-eyebrow">BAGAIMANA ALURNYA</p>',
    unsafe_allow_html=True,
)

st.markdown("### Tiga Tahapan Pelaksanaan")


col1, col2, col3 = st.columns(
    3,
    gap="large",
)


# ============================================================
# TAHAP 1
# ============================================================

with col1:

    dapur_image = IMAGE_DIR / "Dapur.jpeg"

    if dapur_image.exists():
        st.image(
            str(dapur_image),
            use_container_width=True,
        )

    st.markdown(
        "<div class='alur-title'>"
        "01. Persiapan Dapur (SPPG)"
        "</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "SPPG menerima bahan pangan dari pemasok, melakukan pemeriksaan "
        "kualitas, mengolah makanan sesuai standar gizi Badan Gizi Nasional, "
        "kemudian mengemasnya untuk didistribusikan."
    )


# ============================================================
# TAHAP 2
# ============================================================

with col2:

    pengantaran_image = IMAGE_DIR / "pengantaran.jpeg"

    if pengantaran_image.exists():
        st.image(
            str(pengantaran_image),
            use_container_width=True,
        )

    st.markdown(
        "<div class='alur-title'>"
        "02. Distribusi ke Sekolah"
        "</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "Makanan yang telah dikemas didistribusikan dari SPPG ke sekolah "
        "atau kelompok sasaran sesuai jadwal dengan tetap menjaga keamanan "
        "dan kualitas pangan."
    )


# ============================================================
# TAHAP 3
# ============================================================

with col3:

    makan_image = IMAGE_DIR / "Makan_mbg.jpg"

    if makan_image.exists():
        st.image(
            str(makan_image),
            use_container_width=True,
        )

    st.markdown(
        "<div class='alur-title'>"
        "03. Anak-anak Menikmati"
        "</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "Peserta didik menyantap makanan bergizi secara serentak bersama "
        "teman-teman di kelas dengan pengawasan para guru."
    )


# ============================================================
# PEMBATAS
# ============================================================

st.markdown(
    '<hr class="divider-thin"/>',
    unsafe_allow_html=True,
)


# ============================================================
# EKOSISTEM PENYELENGGARAAN MBG
# ============================================================

st.markdown(
    '<p class="section-eyebrow">EKOSISTEM PENYELENGGARAAN MBG</p>',
    unsafe_allow_html=True,
)

st.markdown(
    "### Tiga simpul dalam satu rantai pangan bergizi"
)


# ============================================================
# ICON MITRA PENYELENGGARA
# ============================================================

icon_yayasan = """
<svg width="42" height="42" viewBox="0 0 42 42"
fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="4" y="18" width="34" height="20" rx="3" fill="#173C31"/>
<path d="M21 6 L38 18 H4 Z" fill="#E8A33D"/>
<rect x="17" y="24" width="8" height="14" fill="#FBF6EA"/>
</svg>
"""


# ============================================================
# ICON DAPUR
# ============================================================

icon_dapur = """
<svg width="42" height="42" viewBox="0 0 42 42"
fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="21" cy="24" r="14"
fill="#FBF6EA"
stroke="#173C31"
stroke-width="2.5"/>
<path d="M13 24a8 8 0 0 1 16 0"
fill="#E8A33D"/>
<path d="M15 8c0 3-3 3-3 6
M22 6c0 3-3 3-3 6
M29 8c0 3-3 3-3 6"
stroke="#C1502E"
stroke-width="2.4"
stroke-linecap="round"/>
</svg>
"""


# ============================================================
# ICON SEKOLAH
# ============================================================

icon_sekolah = """
<svg width="42" height="42" viewBox="0 0 42 42"
fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="6" y="16" width="30" height="20" rx="2" fill="#173C31"/>
<rect x="14" y="22" width="6" height="6" fill="#FBF6EA"/>
<rect x="22" y="22" width="6" height="6" fill="#FBF6EA"/>
<path d="M21 6 L36 16 H6 Z" fill="#4C7A5E"/>
<rect x="18" y="28" width="6" height="8" fill="#E8A33D"/>
</svg>
"""


# ============================================================
# DATA EKOSISTEM
# ============================================================

pillars = [

    (
        "01",
        icon_yayasan,
        "Mitra Penyelenggara",
        "Mengelola operasional SPPG, pendanaan, sumber daya manusia, "
        "administrasi, serta memastikan pelaksanaan program sesuai "
        "ketentuan Badan Gizi Nasional.",
        "",
    ),

    (
        "02",
        icon_dapur,
        "Dapur Pemenuhan Gizi (SPPG)",
        "Menyusun menu bergizi sesuai standar BGN, mengadakan bahan pangan, "
        "mengolah makanan, menjaga mutu dan keamanan pangan, serta "
        "mendistribusikan makanan ke sekolah atau kelompok sasaran.",
        "alt",
    ),

    (
        "03",
        icon_sekolah,
        "Sekolah & Penerima",
        "Menerima dan membagikan makanan kepada peserta didik sesuai jadwal, "
        "melakukan pemantauan pelaksanaan, serta memberikan umpan balik "
        "kepada SPPG.",
        "alt2",
    ),
]


# ============================================================
# TAMPILAN CARD EKOSISTEM
# ============================================================

c1, c2, c3 = st.columns(
    3,
    gap="medium",
)


for col, (step, icon, title, desc, cls) in zip(
    [c1, c2, c3],
    pillars,
):

    with col:

        pillar_html = (
            f'<div class="tray-card {cls}">'
            f'<div class="tray-step">{step}</div>'
            f'{icon}'
            f'<h3>{title}</h3>'
            f'<p>{desc}</p>'
            f'</div>'
        )

        st.markdown(
            pillar_html,
            unsafe_allow_html=True,
        )


# ============================================================
# PEMBATAS
# ============================================================

st.markdown(
    '<hr class="divider-thin"/>',
    unsafe_allow_html=True,
)


# ============================================================
# URGENSI & SASARAN
# ============================================================

u_col, s_col = st.columns(
    2,
    gap="large",
)


# ============================================================
# URGENSI
# ============================================================

with u_col:

    st.markdown(
        '<p class="section-eyebrow">Mengapa Penting</p>',
        unsafe_allow_html=True,
    )

    st.markdown("### Urgensi Program MBG")

    st.markdown(
        """
- Menurunkan risiko stunting, kekurangan gizi, dan meningkatkan kualitas asupan gizi peserta didik.
- Meningkatkan kehadiran, konsentrasi belajar, serta mendukung prestasi akademik peserta didik.
- Mendukung tumbuh kembang peserta didik serta mengurangi risiko putus sekolah, terutama di daerah rentan.
- Memberdayakan petani, nelayan, peternak, koperasi, dan UMKM pangan lokal sebagai bagian dari rantai pasok program.
"""
    )


# ============================================================
# SASARAN
# ============================================================

with s_col:

    st.markdown(
        '<p class="section-eyebrow">Siapa yang Dijangkau</p>',
        unsafe_allow_html=True,
    )

    st.markdown("### Sasaran Program MBG")

    st.markdown(
        """
- Peserta didik jenjang **PAUD hingga SMA/SMK** di satuan pendidikan yang tercakup program.
- Ibu hamil dan ibu menyusui sebagai kelompok rawan gizi prioritas.
- Balita sebagai kelompok prioritas dalam pemenuhan gizi.
"""
    )


# ============================================================
# PEMBATAS
# ============================================================

st.markdown(
    '<hr class="divider-thin"/>',
    unsafe_allow_html=True,
)


# ============================================================
# CTA ANALISIS SENTIMEN
# ============================================================

cta_l, cta_r = st.columns(
    [2, 1],
    gap="large",
)


with cta_l:

    st.markdown(
        '<p class="section-eyebrow">Riset Terkait</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "### Bagaimana Persepsi Masyarakat terhadap "
        "Program Makan Bergizi Gratis?"
    )

    st.markdown(
        "Halaman **Analisis Sentimen** menyajikan hasil klasifikasi opini "
        "masyarakat terhadap **Program Makan Bergizi Gratis (MBG)** "
        "berdasarkan data yang diperoleh dari **media sosial X.** "
        "Proses analisis dilakukan menggunakan algoritma "
        "**Multinomial Naive Bayes** dengan pembobotan fitur TF-IDF, "
        "sehingga menghasilkan klasifikasi sentimen ke dalam tiga "
        "kategori, yaitu **positif**, **netral**, dan **negatif**."
    )


with cta_r:

    st.markdown(
        "<br/>",
        unsafe_allow_html=True,
    )

    if st.button(
        "Coba Analisis Sentimen →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/1_Analisis_Sentimen.py"
        )


# ============================================================
# PEMBATAS
# ============================================================

st.markdown(
    '<hr class="divider-thin"/>',
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "MBG Insight dikembangkan sebagai media edukasi dan penelitian. "
    "Informasi mengenai Program Makan Bergizi Gratis mengacu pada sumber "
    "resmi pemerintah, sedangkan hasil analisis sentimen merupakan keluaran "
    "model klasifikasi berbasis data media sosial X dan dapat berubah sesuai "
    "dengan data yang dianalisis."
)

"""Token desain & CSS bersama untuk seluruh halaman aplikasi."""
PINE = "#173C31"          
PINE_SOFT = "#2E5C4B"
MANGO = "#E8A33D"         
MANGO_SOFT = "#F4C878"
CLAY = "#C1502E"          # merah tanah liat - untuk sentimen negatif
SAGE = "#4C7A5E"          # hijau sage - untuk sentimen positif
SAND = "#FBF6EA"          # krem beras - latar
INK = "#22291F"           # teks utama
INK_SOFT = "#5B6459"

BASE_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', sans-serif;
}}

.stApp {{
    background: {SAND};
}}

h1, h2, h3, .display-font {{
    font-family: 'Fraunces', serif;
    color: {INK};
    letter-spacing: -0.01em;
}}

section[data-testid="stSidebar"] {{
    background: {PINE};
}}
section[data-testid="stSidebar"] * {{
    color: {SAND} !important;
}}
section[data-testid="stSidebar"] .stMarkdown p {{
    opacity: 0.85;
}}

/* ---- Hero band ---- */
.mbg-hero {{
    background: linear-gradient(155deg, {PINE} 0%, {PINE_SOFT} 62%, #3E6E58 100%);
    border-radius: 28px;
    padding: 3rem 2.6rem;
    margin-bottom: 2.2rem;
    position: relative;
    overflow: hidden;
}}
.mbg-hero::after {{
    content: "";
    position: absolute;
    right: -60px;
    bottom: -60px;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: radial-gradient(circle, {MANGO} 0%, transparent 70%);
    opacity: 0.35;
}}
.mbg-eyebrow {{
    display: inline-block;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: {MANGO_SOFT};
    background: rgba(255,255,255,0.08);
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    margin-bottom: 1rem;
}}
.mbg-hero h1 {{
    color: #FBF6EA;
    font-size: 2.6rem;
    line-height: 1.12;
    margin: 0 0 0.9rem 0;
    max-width: 720px;
}}
.mbg-hero p {{
    color: #E4EBE3;
    font-size: 1.05rem;
    max-width: 620px;
    line-height: 1.6;
}}

/* ---- Tray-motif card (mimics a divided food tray / nampan) ---- */
.tray-card {{
    background: #FFFFFF;
    border: 1px solid rgba(23,60,49,0.08);
    border-top: 6px solid {MANGO};
    border-radius: 20px;
    padding: 1.6rem 1.5rem 1.4rem 1.5rem;
    height: 100%;
    box-shadow: 0 10px 24px rgba(23,60,49,0.06);
}}
.tray-card.alt {{ border-top-color: {PINE}; }}
.tray-card.alt2 {{ border-top-color: {CLAY}; }}
.tray-card h3 {{
    font-size: 1.15rem;
    margin: 0.2rem 0 0.5rem 0;
}}
.tray-card p {{
    color: {INK_SOFT};
    font-size: 0.94rem;
    line-height: 1.55;
    margin: 0;
}}
.tray-step {{
    font-family: 'Fraunces', serif;
    font-size: 0.85rem;
    font-weight: 600;
    color: {MANGO};
    letter-spacing: 0.04em;
}}

/* ---- Stat pill ---- */
.stat-box {{
    background: #FFFFFF;
    border-radius: 18px;
    padding: 1.3rem 1.2rem;
    text-align: left;
    border: 1px solid rgba(23,60,49,0.08);
}}
.stat-num {{
    font-family: 'Fraunces', serif;
    font-size: 2rem;
    font-weight: 600;
    color: {PINE};
    line-height: 1;
}}
.stat-label {{
    color: {INK_SOFT};
    font-size: 0.86rem;
    margin-top: 0.35rem;
}}

/* section label */
.section-eyebrow {{
    font-weight: 700;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: {SAGE};
    margin-bottom: 0.4rem;
}}

.divider-thin {{
    border: none;
    border-top: 1px solid rgba(23,60,49,0.12);
    margin: 2.4rem 0;
}}

/* result badges for sentiment page */
.badge {{
    display: inline-block;
    padding: 0.5rem 1.1rem;
    border-radius: 999px;
    font-weight: 700;
    font-family: 'Fraunces', serif;
    font-size: 1.05rem;
}}
.badge-positif {{ background: rgba(76,122,94,0.12); color: {SAGE}; }}
.badge-netral {{ background: rgba(232,163,61,0.16); color: #9C6A18; }}
.badge-negatif {{ background: rgba(193,80,46,0.12); color: {CLAY}; }}

footer {{visibility: hidden;}}
</style>
"""

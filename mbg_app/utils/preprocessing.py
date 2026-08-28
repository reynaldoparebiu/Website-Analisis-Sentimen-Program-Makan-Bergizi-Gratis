import re


def clean_text(text: str) -> str:
    """Bersihkan & lower-case teks mentah sebelum di-vectorize."""
    if not isinstance(text, str):
        return ""

    text = text.lower()

    # buang URL
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    # buang mention & hashtag (simbolnya saja, kata tetap dipakai)
    text = re.sub(r"[@#](\w+)", r"\1", text)
    # buang angka
    text = re.sub(r"\d+", " ", text)
    # buang karakter non-alfabet (sisakan spasi)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    # rapikan spasi berlebih
    text = re.sub(r"\s+", " ", text).strip()

    return text

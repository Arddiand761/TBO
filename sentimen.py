import re




# Daftar kata positif dan negatif
positive_words = r'\b(sangat baik|begitu bagus|terlalu senang|sangat suka|hebat sekali|keren banget|asyik sekali|indah sekali|cantik sekali|luar biasa sekali|baik|bagus|senang|suka|hebat|keren|asyik|indah|cantik|luar biasa|menyenangkan|memuaskan)\b'
negative_words = r'\b(tidak|jangan|terlalu|sangat|kurang|buruk|jelek|gagal|rusak|benci|marah|sedih|tidak|jangan|terlalu|sangat|kurang|buruk|jelek|gagal|rusak|benci|marah|sedih)\b'

def sentiment_analysis(text):
    # Mencari pola kata positif
    if re.search(positive_words, text, re.IGNORECASE):
        return "Sentimen Positif"
    # Mencari pola kata negatif
    elif re.search(negative_words, text, re.IGNORECASE):
        return "Sentimen Negatif"
    # Jika tidak ada kata positif atau negatif
    else:
        return "Sentimen Netral"

# Masukan teks dari pengguna
text = input("Masukkan teks untuk analisis sentimen: ")

# Analisis sentimen
res_ult = sentiment_analysis(text)

# Hasil analisis
print(f"Hasil analisis: {res_ult}")

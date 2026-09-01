import random

# Havuzu büyüttük — artık 10 soru var, her çalıştırmada hepsi sorulmayacak.
sorular = [
    {
        "soru": "Python'da bir listeye eleman eklemek için hangi metod kullanılır?",
        "secenekler": {"a": "add()", "b": "append()", "c": "push()", "d": "insert_end()"},
        "dogru_cevap": "b"
    },
    {
        "soru": "Aşağıdakilerden hangisi Python'da bir veri tipi DEĞİLDİR?",
        "secenekler": {"a": "int", "b": "float", "c": "char", "d": "str"},
        "dogru_cevap": "c"
    },
    {
        "soru": "Bir döngüyü erken sonlandırmak için hangi anahtar kelime kullanılır?",
        "secenekler": {"a": "stop", "b": "exit", "c": "break", "d": "end"},
        "dogru_cevap": "c"
    },
    {
        "soru": "JSON dosyasını okumak için hangi fonksiyon kullanılır?",
        "secenekler": {"a": "json.read()", "b": "json.load()", "c": "json.open()", "d": "json.get()"},
        "dogru_cevap": "b"
    },
    {
        "soru": "Python'da yorum satırı hangi karakterle başlar?",
        "secenekler": {"a": "//", "b": "<!--", "c": "#", "d": "**"},
        "dogru_cevap": "c"
    },
    {
        "soru": "Bir fonksiyonu tanımlamak için hangi anahtar kelime kullanılır?",
        "secenekler": {"a": "func", "b": "def", "c": "function", "d": "fn"},
        "dogru_cevap": "b"
    },
    {
        "soru": "Bir string'in uzunluğunu bulmak için hangi fonksiyon kullanılır?",
        "secenekler": {"a": "length()", "b": "size()", "c": "len()", "d": "count()"},
        "dogru_cevap": "c"
    },
    {
        "soru": "Aşağıdakilerden hangisi değiştirilebilir (mutable) bir veri tipidir?",
        "secenekler": {"a": "tuple", "b": "str", "c": "int", "d": "list"},
        "dogru_cevap": "d"
    },
    {
        "soru": "Bir dosyayı açmak için kullanılan fonksiyon hangisidir?",
        "secenekler": {"a": "open()", "b": "read()", "c": "file()", "d": "load()"},
        "dogru_cevap": "a"
    },
    {
        "soru": "Python'da 'True' ve 'False' hangi veri tipine aittir?",
        "secenekler": {"a": "int", "b": "bool", "c": "str", "d": "float"},
        "dogru_cevap": "b"
    },
]

# Her quizde kaç soru sorulacağını burada belirliyoruz.
SORU_SAYISI = 5


def quiz_baslat():
    dogru_sayisi = 0

    # random.sample(liste, kaç_tane), listeden rastgele ve TEKRARSIZ
    # belirtilen sayıda eleman seçer. shuffle'dan farkı: hem seçim hem karıştırma
    # aynı anda yapılıyor, ayrıca havuzdaki TÜM soruları değil sadece bir kısmını alıyoruz.
    secilen_sorular = random.sample(sorular, SORU_SAYISI)

    print("🧠 Python Bilgi Yarışması")
    print(f"Toplam {len(secilen_sorular)} soru var. Başlayalım!\n")

    for index, soru_verisi in enumerate(secilen_sorular, start=1):
        print(f"Soru {index}: {soru_verisi['soru']}")

        for harf in sorted(soru_verisi["secenekler"]):
            print(f"  {harf}) {soru_verisi['secenekler'][harf]}")

        cevap = input("Cevabın (a/b/c/d): ").strip().lower()

        if cevap == soru_verisi["dogru_cevap"]:
            print("✅ Doğru!\n")
            dogru_sayisi += 1
        else:
            dogru_cevap = soru_verisi["dogru_cevap"]
            dogru_metin = soru_verisi["secenekler"][dogru_cevap]
            print(f"❌ Yanlış. Doğru cevap: {dogru_cevap}) {dogru_metin}\n")

    print("--- Sonuç ---")
    print(f"{len(secilen_sorular)} sorudan {dogru_sayisi} tanesini doğru bildin.")

    yuzde = (dogru_sayisi / len(secilen_sorular)) * 100
    print(f"Başarı oranı: %{yuzde:.0f}")


if __name__ == "__main__":
    quiz_baslat()

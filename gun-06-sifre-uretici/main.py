# random modülünü rastgele karakter seçmek için,
# string modülünü ise hazır harf/rakam/sembol gruplarını kullanmak için import ediyoruz.
import random
import string


def sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, sembol):
    # Kullanıcının seçtiği türlere göre karakter havuzunu oluşturuyoruz.
    karakter_havuzu = ""

    if buyuk_harf:
        karakter_havuzu += string.ascii_uppercase  # A-Z
    if kucuk_harf:
        karakter_havuzu += string.ascii_lowercase  # a-z
    if rakam:
        karakter_havuzu += string.digits            # 0-9
    if sembol:
        karakter_havuzu += string.punctuation        # !@#$%^&* gibi semboller

    # Kullanıcı hiçbir tür seçmediyse şifre üretemeyiz.
    if not karakter_havuzu:
        return None

    # random.choice, havuzdan rastgele TEK bir karakter seçer.
    # Bunu bir döngüyle "uzunluk" kadar tekrarlayıp birleştiriyoruz.
    sifre = "".join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    return sifre


def evet_hayir_sor(soru):
    # Kullanıcıdan e/h cevabı alıp True/False'a çeviren yardımcı fonksiyon.
    # Bu fonksiyonu tekrar tekrar yazmamak için ayrı bir fonksiyona koyduk.
    cevap = input(f"{soru} (e/h): ").strip().lower()
    return cevap == "e"


if __name__ == "__main__":
    print("🔐 Şifre Üretici")

    try:
        uzunluk = int(input("Şifre uzunluğu (örn. 12): "))
    except ValueError:
        print("⚠️ Geçersiz sayı, varsayılan olarak 12 kullanılıyor.")
        uzunluk = 12

    buyuk_harf = evet_hayir_sor("Büyük harf olsun mu?")
    kucuk_harf = evet_hayir_sor("Küçük harf olsun mu?")
    rakam = evet_hayir_sor("Rakam olsun mu?")
    sembol = evet_hayir_sor("Sembol olsun mu? (!@#$ gibi)")

    sifre = sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, sembol)

    if sifre is None:
        print("⚠️ En az bir karakter türü seçmelisin!")
    else:
        print(f"\n🔑 Üretilen şifre: {sifre}")

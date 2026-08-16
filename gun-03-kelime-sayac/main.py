def dosya_analiz_et(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        kelimeler = icerik.split()
        kelime_sayisi = len(kelimeler)
        karakter_sayisi = len(icerik)
        satir_sayisi = icerik.count('\n') + 1

        print(f"Dosya Adı: {dosya_adi}")
        print(f"Kelime Sayısı: {kelime_sayisi}")
        print(f"Karakter Sayısı: {karakter_sayisi}")
        print(f"Satır Sayısı: {satir_sayisi}")


if __name__ == "__main__":
    dosya_adi = input("Analiz edilecek dosyanın adını girin: ")
    dosya_analiz_et(dosya_adi)

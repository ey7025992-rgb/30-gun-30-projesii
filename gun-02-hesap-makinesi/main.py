def hesap_makinesi():
    print("🧮 Basit Hesap Makinesi")
    print("İşlemler: + (toplama), - (çıkarma), * (çarpma), / (bölme)")
    print("Çıkmak için 'q' yaz")

    while True:
        sayi1_giris = input("\nBirinci sayı (çıkmak için q): ")
        if sayi1_giris == "q":
            print("Görüşürüz! 👋")
            break

        islem = input("İşlem seç (+, -, *, /): ")
        sayi2_giris = input("İkinci sayı: ")

        sayi1 = float(sayi1_giris)
        sayi2 = float(sayi2_giris)

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                print("⚠️ Sıfıra bölme yapılamaz!")
                continue
            sonuc = sayi1 / sayi2
        else:
            print("⚠️ Geçersiz işlem!")
            continue

        print(f"Sonuç: {sonuc}")


if __name__ == "__main__":
    hesap_makinesi()

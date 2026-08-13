import random

# Bu fonksiyon, tüm oyun mantığını içeriyor.
# Programı çalıştırdığımızda en altta çağrılıyor.


def oyunu_baslat():
    gizli_sayi = random.randint(1, 100)
    deneme_sayisi = 0
    tahmin_edildi = False

    print("1 ile 100 arasında bir sayı tuttum. Bilebilir misin?")

    while not tahmin_edildi:
        try:
            tahmin = int(input("Tahminin: "))
        except ValueError:
            print("Şütfen geçerli bir sayı gir!")
            continue

        deneme_sayisi += 1

        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene.")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı dene.")
        else:
            print(
                f"Bildiniz! {gizli_sayi} imiş. Toplam {deneme_sayisi} denemede buldun.")
            tahmin_edildi = True


if __name__ == "__main__":
    oyunu_baslat()

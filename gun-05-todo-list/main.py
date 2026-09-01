# json modülü, verileri dosyaya kaydetmek ve dosyadan okumak için kullanılır.
# Python'daki liste/sözlük gibi verileri .json dosyasına yazıp geri okuyabiliriz.
import json
import os

DOSYA_ADI = "gorevler.json"


def gorevleri_yukle():
    # Dosya daha önce oluşturulmadıysa boş bir liste döndür.
    if not os.path.exists(DOSYA_ADI):
        return []

    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        return json.load(dosya)


def gorevleri_kaydet(gorevler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        # ensure_ascii=False, Türkçe karakterlerin bozulmadan kaydedilmesini sağlar.
        # indent=2, dosyayı okunaklı (düzenli girintili) hale getirir.
        json.dump(gorevler, dosya, ensure_ascii=False, indent=2)


def gorevleri_listele(gorevler):
    if not gorevler:
        print("📭 Hiç görev yok.")
        return

    for index, gorev in enumerate(gorevler, start=1):
        durum = "✅" if gorev["tamamlandi"] else "⬜"
        print(f"{index}. {durum} {gorev['baslik']}")


def gorev_ekle(gorevler):
    baslik = input("Yeni görev: ").strip()
    if baslik:
        gorevler.append({"baslik": baslik, "tamamlandi": False})
        print("✅ Görev eklendi.")
    else:
        print("⚠️ Boş görev eklenemez.")


def gorev_tamamla(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        secim = int(input("Tamamlandı olarak işaretlenecek görev numarası: "))
        gorevler[secim - 1]["tamamlandi"] = True
        print("✅ Görev tamamlandı olarak işaretlendi.")
    except (ValueError, IndexError):
        print("⚠️ Geçersiz numara.")


def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        secim = int(input("Silinecek görev numarası: "))
        silinen = gorevler.pop(secim - 1)
        print(f"🗑️ '{silinen['baslik']}' silindi.")
    except (ValueError, IndexError):
        print("⚠️ Geçersiz numara.")


def menu_goster():
    print("\n--- To-Do List ---")
    print("1. Görevleri listele")
    print("2. Görev ekle")
    print("3. Görevi tamamlandı işaretle")
    print("4. Görev sil")
    print("5. Çıkış")


if __name__ == "__main__":
    gorevler = gorevleri_yukle()

    while True:
        menu_goster()
        secim = input("Seçim: ").strip()

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
            gorevleri_kaydet(gorevler)
        elif secim == "3":
            gorev_tamamla(gorevler)
            gorevleri_kaydet(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
            gorevleri_kaydet(gorevler)
        elif secim == "5":
            print("Görüşürüz! 👋")
            break
        else:
            print("⚠️ Geçersiz seçim.")

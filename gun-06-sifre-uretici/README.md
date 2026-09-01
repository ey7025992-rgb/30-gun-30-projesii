# Şifre Üretici

Kullanıcının belirlediği uzunluk ve karakter türlerine (büyük harf, küçük harf, rakam, sembol) göre rastgele şifre üreten bir araç.

## Özellikler
- İstenen şifre uzunluğunu belirleme
- Büyük harf, küçük harf, rakam, sembol kullanımını ayrı ayrı açıp kapatma
- Hiçbir tür seçilmezse uyarı verme

## Çalıştırmak için
```bash
python main.py
```

## Örnek kullanım

Şifre uzunluğu (örn. 12): 12
Büyük harf olsun mu? (e/h): e
Küçük harf olsun mu? (e/h): e
Rakam olsun mu? (e/h): e
Sembol olsun mu? (!@#$ gibi) (e/h): e

🔑 Üretilen şifre: Xk9#mPz2Qw@1



## Not
Şifredeki karakterler tamamen rastgele seçildiği için, kısa şifrelerde (örn. 4 karakter) seçilen türlerden biri (örn. rakam) hiç görünmeyebilir. Bu bir hata değil, olasılık meselesidir — uzunluk arttıkça bu ihtimal azalır.
# Kullanıcıdan Veri Alma Yöntemi
sayi1 = float(input("Birinici Sayiyi Giriniz:"))
sayi2 = float(input("İkinci Sayiyi Giriniz:"))
islem = str(input("Yapmak istediginiz islem giriniz(+,-,/,*):  "))


# İşlem Kontrol birimi if else elif yapısı
if islem == "+":
    sonuc = (sayi1 + sayi2)

elif islem == "-":
    sonuc = sayi1 - sayi2

elif islem == "*":
    sonuc = sayi1 * sayi2

elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
    else:
        print("Islem sonucu belirsiz cikiyor sayi2 sıfır olmasın")
else:
    print("Gecersiz Islem Girdiniz")

print(f"Islem Sonucnuz:  {sonuc}")
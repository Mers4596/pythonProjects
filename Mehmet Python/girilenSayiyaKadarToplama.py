print("Girilen Sayiya Kadar Olan Sayilari Toplama")
girilenSayi = int(input("Lutfen Bir Sayi Giriniz:"))

toplam = 0
for  i in range(1, girilenSayi+1):
    toplam = toplam + i
print(f"Girdiginiz Sayiya Kadar Olan Toplam: {toplam}")


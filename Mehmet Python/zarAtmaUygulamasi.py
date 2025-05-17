import random

print("*-*-*-*-*-*-*-* ZAR ATMA OYUNUNA HOŞGELDİNİZ *-*-*-*-*-*-*-*")

oyuncu1 = input("Lütfen Birinci Oyuncunun Adini Giriniz: ")
oyuncu2 = input("Lütfen İkinci Oyuncunun Adini Giriniz: ")


oyuncu1_toplam = 0
oyuncu2_toplam = 0

for tur in range(1, 4):
    print(f"{tur}.TUR 'Herkese Bol Şans' \n")
    oyuncu1_zar = random.randint(1 , 6)
    oyuncu2_zar = random.randint(1 , 6)

    print(f"{oyuncu1} ' in Attiği Zar: {oyuncu1_zar}")
    print(f"{oyuncu2} ' in Attiği Zar: {oyuncu2_zar}")

    oyuncu1_toplam += oyuncu1_zar
    oyuncu2_toplam += oyuncu2_zar

print("*-*-*-*-*-*-*-*-*-*-* OYUN BİTTİ *-*-*-*-*-*-*-*-*-*-*")

if oyuncu1_toplam > oyuncu2_toplam:
    print(f"{oyuncu1} KAZANDII TEBRİKLER !!!!")
elif oyuncu1_toplam < oyuncu2_toplam:
    print(f"{oyuncu2} KAZANDII TEBRİKLER !!!!")
else:
    print("ÇOK BÜYÜK ŞANS HER İKİ OYUNCUDA BERABERE KALDI")








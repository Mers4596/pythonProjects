sayilar = []

for i in range(5): # 0 1 2 3 4 toplam 5 indeks var dikkat
    sayi = int(input(f"{i+1}. sayiyi giriniz: "))
    sayilar.append(sayi)
print("Girdiğiniz sayilar", sayilar)
print("En Büyük Sayı:", max(sayilar) )    
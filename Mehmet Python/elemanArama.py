t_Şehirler = ["Kayseri" , "Samsun", "Balıkesir", "Adana", "Ordu", "Konya", "Tekirdağ", "İstanbul"]

while True:
    print("\n1.Arama")
    print("\n2.Cikis")
    
    secim = int(input("Lütfen bir seçim yapiniz:"))

    if secim == 1:
        arama = str(input("Aramak İstediğiniz sehiri giriniz:"))
        if arama in t_Şehirler:
            print(f" {arama}, listede mevcut")
        else:
            print(f"{arama}, listede mevcut değil")

    elif secim == 2:
        print("Çıkış Yapılıyor")
        break

    else:
        print("Hatalı bir işlem girdiniz lütfen tekrar deneyiniz")






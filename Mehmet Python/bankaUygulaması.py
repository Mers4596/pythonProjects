para = 1000

def paraÇekmeMiktari(miktar):
    global para

    if miktar > para:
        print("Yetersiz bakiye Güncel bakiyeniz {para}")
    else:
        para = para - miktar
        print(f"{miktar}TL para çekildi kalan bakiye {para}TL")     

    return para   
    
def paraYatirmaMiktari(miktar):
    global para
    para = para + miktar
    print(f"{miktar}TL para yatirdiniz güncel bakiyeniz{para}TL")
    return para   



def main():
    global para
    while True:
        print("\n---Banka Uygulamasina Hoş Geldiniz---\n")
        print("1. Para Çekmek")
        print("2. Para Yatirmak")
        print("3. Tüm Bakiyeyi Görmek")
        print("4. Çikiş Yapmak\n")

        try:
            secenek = int(input("Hangi işlemi seçeceğinizi Giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayi giriniz:")
            continue
        if secenek == 1:
            miktar = int(input("Ne kadar Çekmek Istediğinizi Giriniz:"))
            paraÇekmeMiktari(miktar)
                
        elif secenek == 2:
            miktar = int(input("Ne kadar para yatirmak istedğinizi giriniz:"))
            paraYatirmaMiktari(miktar)
           
        elif secenek == 3:
            print(f"Güncel bakiyeniz: {para}")
        elif secenek == 4:
            print("Banka Uygulamasindan çikiş yapiliyor")
            break
        else:
            print("!!Geçersiz bir karakter tuşlamsini yaptiniz lütfen tekrar deneyiniz!!")
if __name__ == "__main__":
    main()
 

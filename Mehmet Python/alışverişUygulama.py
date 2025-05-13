ürün_listesi = []

def ürün_ekle(eklenen_ürün):
  ürün_listesi.append(eklenen_ürün)
  print(f"{eklenen_ürün},Ürün listesine Başiryla Eklenmiştir")
  return ürün_ekle

def ürün_sil(silinen_ürün):
  if silinen_ürün in ürün_listesi:
    print(f"{silinen_ürün}, Başariyla Listeden Silinmiştir")
    ürün_listesi.remove(silinen_ürün)
  else: 
    print("Silemek İstediğiniz Ürün, Ürün Listesinde Bulunmamaktadir. Lütfen Tekrar Deneyiniz")
  return ürün_sil

def tümliste_göster():
  
  if ürün_listesi:

    print("*-*-*-*-*-GÜNCEL ÜRÜN LİSTENİZ*-*-*-*-*-")
    sayaç = 1
    for ürün in (ürün_listesi):
      print(f"{sayaç}.{ürün}")
      sayaç = sayaç + 1

  else:
    print("Ürün Listenizde Bir Şey Bulunmamaktadir Lütfen Ürün Ekleyiniz. ") 
    return ürün_listesi       



def main():
 print("\n *-*-*-*-*-*-*-*ALIŞVERİŞ UYGULAMSINA HOŞGELDİNİZ*-*-*-*-*-*-*-* \n")
  
 while True:
    print("\n 1. Ürün Ekle")
    print("2. Ürün Sil")
    print("3. Tüm Listeyi Görüntüle")
    print("4. Çikiş")

    secenek = int(input("Lütfen Hangi İşlemi Yapacağinizi Tuşlayiniz: "))

    if secenek == 1:
       ürün = str(input(f"Lütfen Eklemek İstedeğiniz Ürünü Giriniz: "))
       ürün_ekle(ürün)

    elif secenek == 2:
      ürün = str(input(f"Lütfen Silmek İstediğiniz Ürünü Giriniz: "))
      ürün_sil(ürün)

    elif secenek == 3:
      tümliste_göster()

    elif secenek == 4:
      print("Aişveriş Uygulamsindan Çikiş Yapiliyor...")
      break
    else:
      print("Geçersiz Bir Değer Girdiniz Lütfen (1 ile 4) Arsinda Bir Değer Giriniz")

if __name__ == "__main__":
  main()


      
      
           

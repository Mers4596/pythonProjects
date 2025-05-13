import random
playlist = []

def sarkiEkle(eklenen_sarki):
    playlist.append(eklenen_sarki)
    print(f"{eklenen_sarki}, playlistte başariyla eklenmiştir")
    return playlist

def sarkiSil(silinen_sarki):
    if silinen_sarki in playlist:
        playlist.remove(silinen_sarki)
        print(f"{silinen_sarki} playlistten başariyla kaldirilmiştir")
    else:
        print("Silmek İstediginiz Sarki Playlistte Bulunmamaktadir Lütfen Tekrar Deneyiniz")
    return playlist

def tümListeGöster():
    if playlist:
        print("****Güncel Tüm Playlist****")
        for index in enumerate(playlist, start=1):
            print(f"{index}.{playlist}")
        
    else:
        print("Listeniz Boş. Lütfen Şarki Ekle Kismindan Şarki ekleyiniz")
    return playlist    

    


def rasgeleSarkiCal(calinan_sarki):
    calinan_sarki = random.choice(playlist)
    if calinan_sarki in playlist:
        print(f"\n Şimdi Çalan Şarki: {calinan_sarki}")
    else:
        print("Playlistiniz Boş. Lütfen Şarki Ekleyiniz")
    return playlist            


def main():
    

    while True:
        print("Playlist Uygulamsina Hoşgeldiniz")
        print("1. Şarki Ekle")
        print("2. Şarki Sil")
        print("3. Tüm Listeyi Göster")
        print("4. Rastgele Şarki Çal")
        print("5. Çikis")

        secenek = int(input("Lütfen Bir Mod Seçiniz: "))
        if secenek == 1:
            sarki = str(input("Sarki Adini Giriniz"))
            sarkiEkle(sarki)
        elif secenek == 2:
            sarki = str(input("Lütfen Silmek İstedeğimiz Şarkiyi Giriniz:"))
            sarkiSil(sarki)
        elif secenek == 3:
            tümListeGöster()
        elif secenek == 4:
            rasgeleSarkiCal(sarki)
        elif secenek == 5:
            print("Playlist Uygulamsindan Çikis Yapiliyor...")
            break
        else:
            print("Lütfen Geçerli bir değer giriniz!!!")        
if __name__ == "__main__":
    main()




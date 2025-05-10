def not_defteri(): #adında bir fonksiyon tanımlanıyor. Tüm işlemler bu fonksiyon içinde yapılacak.
    while True: #Kullanıcının çıkış yapmak isteyene kadar menüde kalması sağlanıyor.
        print("\n1. Not yaz ve kaydet") 
        print("2. Notlari Görüntüle")
        print("3. Notlari Sil")
        print("4. Not Ara")  
        print("5. Not Sayisi Göster")  
        print("6. Cikis")

        secim = input("Lütfen bir Secim Yapiniz: ")

        if secim == "1":
            not_metni = input("Notunuz Yaziniz:")
            # With open(....) as .... Python'da dosya açma ve otomatik kapatma işlemleri için kullanılır.
             # Buradaki "a" bir "kip" tir yani dosya açma modu "a" nın işlevi ise eklemedir.
             # as degisken: Bu dosyaya erişmek için kullanılacak değişken.
            with open("notlar.txt" , "a" , encoding="utf-8") as dosya:
                dosya.write(not_metni + "\n")
            print("Dosya Kaydedildi!")

        elif secim == "2":
            try:
                with open("notlar.txt" , "r", encoding="utf-8") as dosya: 
                    notlar = dosya.read()
                    print("\nKayitli Notlar:\n" + notlar)
            except FileNotFoundError:
                print("Henüz Hic Dosya Kaydedilmedi.")

        elif secim == "3":
            with open("notlar.txt","w",encoding="utf-8") as dosya:
                dosya.write(" ")
            print("Tüm Notlar silindi")

        elif  secim == "4":
            aranan = input("Aramak istediğiniz kelimeyi giriniz: ")
            try:
                with open("notlar.txt", "r" ,encoding = "utf-8") as dosya:
                    satirlar = dosya.readlines()
                    eslesen = [s for s in satirlar if aranan in s]
                    if eslesen:
                        print("Eşleşen Notlar")
                        for e in eslesen:
                            print(e.strip())
                    else:
                        print("Eslesen Notunuz Bulunmamaktadir")
            except FileNotFoundError:
                print("Henüz hiç not kaydedilmemiş!!!")

        elif secim == "5":
          try:
            with open("notlar.txt", "r" , encoding="utf-8") as dosya:
                satir_sayisi = len(dosya.readlines())
                print(f"Toplam {satir_sayisi} not var.")
          except FileNotFoundError:
              print("Henüz hiç not kaydedilmemiş.")                                         

        elif secim == "6":
            print("Çikiş Yapiliyor...")
            break        
        else:
            print("Hatali Bir Secim Yaptiniz Lütfen Tekrar Deneyiniz!!!")
#uygulama calistırır:            
not_defteri()            
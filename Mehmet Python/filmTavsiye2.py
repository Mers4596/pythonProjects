import random


while True:
        print("1. aksiyon")
        print("2. komedi")
        print("3. bilim kurgu")
        print("4. dram")
        print("5. animasyon")
        print("6. korku")
        print("7. romantik")
        print("8. cikis")

        secenek = str(input("Lütfen Seçmek Istediğiniz Türü Giriniz: "))

        if secenek == "1":
            filmler = ["John Wick, Mad Max: Fury Road, The Dark Knight, Gladiator, Inception, Die Hard, Mission Impossible"]

        elif secenek == "2":
            filmler = ["The Hangover, Superbad, Step Brothers, The Mask, Home Alone, Yes Man, Mr. Bean's Holiday"]

        elif secenek == "3":
            filmler = ["Interstellar", "The Matrix", "Inception", "Blade Runner 2049", "Arrival", "Tenet", "Ready Player One"]

        elif secenek == "4":
            filmler = ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness", "Titanic", "Green Mile", "Joker", "Whiplash"]
        
        elif secenek == "5":
            filmler = ["Toy Story", "Frozen", "Shrek", "Finding Nemo", "Zootopia", "Coco", "Ratatouille"]

        elif secenek == "6":
            filmler = ["The Conjuring", "Insidious", "Annabelle", "IT", "The Exorcist", "A Quiet Place", "Hereditary"]

        elif secenek == "7":
            filmler = ["The Notebook", "La La Land", "Titanic", "Me Before You", "A Walk to Remember", "Love Actually", "Crazy Rich Asians"]
 
        elif secenek == "8":
            print("Film Tavsiye Uygulamsindan Çikiliyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-8 arasinda bir sayi girin.")
            continue

        if secenek in ["1","2","3","4","5","6","7","8"]:
            film = random.choice(filmler)
            print(f"\nÖnerilen Film: {film}")



        


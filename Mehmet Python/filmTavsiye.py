import random
film_listesi = {
"aksiyon" : ["Mad Max: Fury Road", "John Wick", "The Dark Knight"],
"komedi" : ["Recep İvedik", "The Mask", "Superbad", "Step Brothers"],
"dram" : [" The Shawshank Redemption", "Forrest Gump", "The Godfather"],
"bilim kurgu" : ["Insterstellar", "Inception", "The Matrix"]
}

tür = str(input("Lütfen bir hangi türde film izlemk istediğinizi giriniz: "))

if tür in film_listesi:
    önerilen_film = random.choices(film_listesi[tür])
    print(f"[{tür} Kategorisde En Çok Önerilen Film: {önerilen_film}]")
else:
    print(f"seçtiğiniz tür: {tür}. film film listesinde bulunmamaktadir.")     
    
sozluk = {
   "python": "Bir programlama dilidir.",
   "algoritma": " Belirli vir problemi çözümü kavuşturacak mantıksal adımlar dizisi",
   "data": "bilgi,veri"
}

kelime = input("Anlamini Ogrenmek Istediginiz Bir Kelime Giriniz: ")

if kelime in sozluk:
    print(f"{kelime} : {sozluk[kelime]}")
else:
    print("Sözlükte Bulunamadi")    
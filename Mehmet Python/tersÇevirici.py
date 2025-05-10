cümle = str(input("Lütfen ters çevirmek istediğiniz cümleyi giriniz:"))
kelimeler = cümle.split() # cümleyi kelimlere ayırır
kelimeler.reverse() # kelimleri ters çevirir
ters_cümle =  " " .join(kelimeler)
print(f"Ters Hali: " , ters_cümle)
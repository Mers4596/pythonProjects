import json
from difflib import get_close_matches as yakin_sonuclari_getir

# json.dump()  Herhangi bir json versini dosyaya yazdırabiliyoruz ayrıca kisileştirebiliriz
# json.load(./veritanbanı.json)  Dosya Yüklemek için


def veritabanini_yükle():
    with open('C:\\Users\\Mehmet Ersolak\\Desktop\\Akıllı_Chatbot\\veritabanı.json','r', encoding="utf-8") as dosya:
        return json.load(dosya)
    
def veritabanina_yaz(veriler):
    with open('C:\\Users\\Mehmet Ersolak\\Desktop\\Akıllı_Chatbot\\veritabanı.json','w') as dosya:
        json.dump(veriler,dosya,indent=2)

def yakin_sonnuc_bul(soru, sorular):
    soru = soru.lower().strip()

    # Sorular içinde liste olanları düzleştir
    duzeltilmis_sorular = []
    for s in sorular:
        if isinstance(s, list):
            duzeltilmis_sorular.extend([v.lower().strip() for v in s])
        else:
            duzeltilmis_sorular.append(s.lower().strip())

    eslesen = yakin_sonuclari_getir(soru, duzeltilmis_sorular, n=1, cutoff=0.6)
    return eslesen[0] if eslesen else None

def cevabini_bul(soru, veritabani):
    soru = soru.lower().strip()
    for soru_cevaplar in veritabani["sorular"]:
        # Eğer veri bir listeyse tümünü kontrol et
        if isinstance(soru_cevaplar["soru"], list):
            for varyasyon in soru_cevaplar["soru"]:
                if varyasyon.lower().strip() == soru:
                    return soru_cevaplar["cevap"]
        else:
            if soru_cevaplar["soru"].lower().strip() == soru:
                return soru_cevaplar["cevap"]
    return None


def chat_bot():
    veritabani = veritabanini_yükle()
    
    while(True):
        soru = input("siz: ")

        if soru == "çık":
            break

        gelen_sonuc = yakin_sonnuc_bul(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"] ])    

        if gelen_sonuc:
            verilecek_cevap = cevabini_bul(gelen_sonuc, veritabani)
            print(f"Bot: {verilecek_cevap}")
        else:
            print("Bot: Bunu Nasıl Cevaplayacağımı Bilmiyorum. Öğretir misiniz ?")
            yeni_cevap = input("Öğretmek İçin Yazabilirsiniz veya 'geç' diyebilirsiniz.")

            if yeni_cevap != 'geç':
                veritabani["sorular"].append({
                "soru": soru,
                "cevap": yeni_cevap
                })
                veritabanina_yaz(veritabani)
                print("Bot: Teşekkürler, sayenizde bir şey öğrendim..")







if __name__ == '__main__':
    chat_bot()
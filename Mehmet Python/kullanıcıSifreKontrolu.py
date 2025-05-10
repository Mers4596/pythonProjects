dogru_sifre = "12345"
dogru_kullanici_adi = "Admin"



deneme = 0
max_Deneme = 4


while deneme < max_Deneme:
    kullanici_Girdigi_Ad = input("Lütfen Kullanıcı Adını Giriniz: ")
    kullanici_Girdigi_Sifre = input("Lütfen Şifrenizi Giriniz: ")

    if dogru_sifre == kullanici_Girdigi_Sifre and dogru_kullanici_adi == kullanici_Girdigi_Ad:
        print("Giriş Başarılı")
        break
    elif dogru_kullanici_adi != kullanici_Girdigi_Ad and dogru_sifre != kullanici_Girdigi_Sifre:
        print("Girdiğiniz Kullanıcı Adı ve Şifre Yanlış")
    elif dogru_kullanici_adi != kullanici_Girdigi_Ad:
        print("Kullanıcı Adınız Yanlış")
    elif dogru_sifre != kullanici_Girdigi_Sifre:
        print("Girdiğiniz Şifre Yanlış")
    deneme += 1
    kalan_hak = max_Deneme - deneme

    if deneme < max_Deneme:
        print(f"{kalan_hak} hakkiniz kaldi")
    else:
        print(f"{max_Deneme} hakkiniz doldu sistem bloke oldu")

sayi = int(input("Bir Sayi Giriniz: "))

if sayi > 1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print(f"{sayi} Asal Sayi Değildir! ! !")
            break

    else:
        print(f"{sayi}, Asal Sayidir")
                
else:
    print("Lütfen 1 den büyük bir sayi giriniz")

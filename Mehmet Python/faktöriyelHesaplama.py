sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayiyi giriniz:"))
fak = 1
for i in range(1,sayi + 1):
    fak = fak * i
print(f"{sayi} nin faktöriyeli: {fak}")

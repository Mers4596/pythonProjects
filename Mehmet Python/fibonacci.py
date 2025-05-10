n = int(input("Kaç terim istiyorsunuz?")) # kaç terim istendiğini kullanıcıdan alırız
a,b = 0,1 # ilk değer 0 ikinci değer 1 olsun
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
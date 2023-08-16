def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bölme işlemi sıfıra bölme hatası verir."
    return x / y

print("İşlem seçenekleri:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    secim = input("Yapmak istediğiniz işlemi seçiniz (1/2/3/4): ")

    if secim in ('1', '2', '3', '4'):
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if secim == '1':
            print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
        elif secim == '2':
            print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
        elif secim == '3':
            print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
        elif secim == '4':
            print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
    else:
        print("Geçersiz giriş. Lütfen 1, 2, 3 veya 4 seçeneğinden birini giriniz.")

    devam = input("Başka bir hesaplama yapmak istiyor musunuz? (Evet/Hayır): ")
    if devam.lower() != 'evet':
        break

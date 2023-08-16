import random

def kazanan(secim_oyuncu, secim_bilgisayar):
    if secim_oyuncu == secim_bilgisayar:
        return "Berabere!"
    elif (secim_oyuncu == "taş" and secim_bilgisayar == "makas") or \
         (secim_oyuncu == "kağıt" and secim_bilgisayar == "taş") or \
         (secim_oyuncu == "makas" and secim_bilgisayar == "kağıt"):
        return "Oyuncu kazandı!"
    else:
        return "Bilgisayar kazandı!"

def main():
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        secim_oyuncu = input("Taş mı, kağıt mı, makas mı? (Çıkış için 'q'): ").lower()

        if secim_oyuncu == "q":
            print("Oyun sona erdi.")
            break

        if secim_oyuncu not in secenekler:
            print("Geçersiz bir seçim yaptınız. Lütfen taş, kağıt veya makas seçin.")
            continue

        secim_bilgisayar = random.choice(secenekler)

        print("Oyuncunun seçimi:", secim_oyuncu)
        print("Bilgisayarın seçimi:", secim_bilgisayar)

        sonuc = kazanan(secim_oyuncu, secim_bilgisayar)
        print(sonuc)

if __name__ == "__main__":
    main()


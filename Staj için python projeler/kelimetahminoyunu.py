import random

def kelime_sec():
    kelimeler = ["python", "programlama", "bilgisayar", "laptop", "modem", "klavye", "monitör"]
    return random.choice(kelimeler)

def tahmin_alanı(gizli_kelime, tahmin_edilen_harfler):
    tahmin_alani = ""
    for harf in gizli_kelime:
        if harf in tahmin_edilen_harfler:
            tahmin_alani += harf
        else:
            tahmin_alani += "_"
    return tahmin_alani

def oyun():
    gizli_kelime = kelime_sec()
    tahmin_edilen_harfler = []
    tahmin_hakki = 5

    print("Kelime tahmin oyununa hoş geldiniz!")
    print(tahmin_alanı(gizli_kelime, tahmin_edilen_harfler))

    while True:
        tahmin = input("Bir harf tahmin edin: ").lower()

        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten tahmin ettiniz.")
        else:
            tahmin_edilen_harfler.append(tahmin)
            if tahmin in gizli_kelime:
                print("Doğru tahmin!")
            else:
                print("Yanlış tahmin!")
                tahmin_hakki -= 1
                if tahmin_hakki == 0:
                    print("Tahmin hakkınız kalmadı. Doğru kelime '{}' idi.".format(gizli_kelime))
                    break

        tahmin_alani_str = tahmin_alanı(gizli_kelime, tahmin_edilen_harfler)
        print(tahmin_alani_str)

        if "_" not in tahmin_alani_str:
            print("Tebrikler! Kelimeyi doğru tahmin ettiniz.: '{}'".format(gizli_kelime))
            break

if __name__ == "__main__":
    oyun()

def main():
    dogru_ad = "Alp Eren"
    harf_indeksi = 0
    
    print("Adınızı harf harf tahmin etme oyununa hoş geldiniz!")
    
    while harf_indeksi < len(dogru_ad):
        tahmin = input(f"{harf_indeksi+1}. harfi tahmin edin: ")

        if tahmin.lower() == dogru_ad[harf_indeksi].lower():
            print("Doğru tahmin ettiniz!")
            harf_indeksi += 1
        else:
            print("Yanlış tahmin ettiniz. Tekrar deneyin.")

    print("Tebrikler! Adınızı doğru tahmin ettiniz: " + dogru_ad)

if __name__ == "__main__":
    main()

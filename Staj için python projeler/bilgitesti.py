def bilgi_testi():
    sorular = [
        {
            "soru": "Dünyanın en uzun nehrinin adı nedir?",
            "cevap": "nil"
        },
        {
            "soru": "Einstein'ın ünlü denkleminde E harfi neyi temsil eder?",
            "cevap": "enerji"
        },
        {
            "soru": "Türkiyenin en engin iş adamı kimdir?",
            "cevap": "İbrahim Erdemoğlu"
        },
        {
            "soru": "Türkiyenin en kalabalık nüfusu hangi şehirdir?",
            "cevap": "İstanbul"
        },
        {
            "soru": "Türkiye'nin başkenti hangi şehirdir?",
            "cevap": "ankara"
        },
        {
            "soru": "İnsan vücudundaki en büyük organ nedir?",
            "cevap": "cilt"
        },
        {
            "soru": "Kraliyet ailesinin en genç üyesi kimdir?",
            "cevap": "archie"
        }
    ]
    
    dogru_cevaplar = 0

    print("Bilgi Testine Hoş Geldiniz!")
    print("Cevap verirken harf büyük küçüklüğüne dikkat ediniz.")
    print("Bol şans dilerim.")
    
    for soru_no, soru_dict in enumerate(sorular, start=1):
        print(f"\nSoru {soru_no}: {soru_dict['soru']}")
        kullanici_cevap = input("Cevabınız: ")
        
        if kullanici_cevap.lower() == soru_dict["cevap"].lower():
            print("Doğru cevap! +1 puan\n")
            dogru_cevaplar += 1
        else:
            print(f"Yanlış cevap. Doğru cevap: {soru_dict['cevap']}\n")

    print(f"Testi tamamladınız! Toplam doğru cevap sayısı: {dogru_cevaplar}/{len(sorular)}")

if __name__ == "__main__":
    bilgi_testi()

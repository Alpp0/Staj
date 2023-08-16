import time
import winsound

def metin_tabanli_saat():
    simdi = time.localtime()
    saat = time.strftime("%H:%M:%S", simdi)
    print(f"Aktüel Saat: {saat}")

def zamanlayici(sure):
    print(f"Zamanlayıcı {sure} saniye boyunca çalışacak.")
    baslangic = time.time()
    
    while True:
        metin_tabanli_saat()
        gecen_sure = time.time() - baslangic
        
        if gecen_sure >= sure:
            metin_tabanli_saat()
            winsound.Beep(1000, 1000)  
            print("Zaman doldu! Süre sona erdi.")
            break
        
        if sure - gecen_sure <= 60 and sure - gecen_sure >= 50:
            print("Son 1 dakika kaldı.")
        if sure - gecen_sure <= 10:
            print(f"Son {int(sure - gecen_sure)} saniye kaldı.")
        
        time.sleep(1)

def main():
    print("Metin Tabanlı Saat ve Zamanlayıcı Uygulamasına Hoş Geldiniz!")
    while True:
        print("Seçiminizi yapın:")
        print("1 - Metin Tabanlı Saat")
        print("2 - Zamanlayıcı")
        print("3 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            metin_tabanli_saat()
        elif secim == "2":
            sure = int(input("Zamanlayıcı için süre (saniye cinsinden) girin: "))
            zamanlayici(sure)
        elif secim == "3":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

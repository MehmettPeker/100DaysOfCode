boy_uzunlugu = int(input("Boy uzunluğunuzu giriniz: "))
bilet_fiyati = 0

if boy_uzunlugu >= 120:
    print("Hızlı trene binebilirisiniz")
    yas = int(input("Yaşınızı giriniz: "))

    if yas < 12:
        bilet_fiyati = 5
        print("Çocuk bilet ücreti 5$")
    elif yas < 18:
        print("Genç bilet ücreti 7$")
        bilet_fiyati = 7
    else:
        print("Yetişkin bilet fiyatı 12$")
        bilet_fiyati = 12

    fotograf_hizmeti= input("Fotoğraf hizmeti ister misiniz?")
    if fotograf_hizmeti == "y":
        bilet_fiyati += 3
    else:
        bilet_fiyati 
    
    print(f"Toplam bilet tutarınız: ${bilet_fiyati}")
else:
    print("Trene Binemezsiniz")
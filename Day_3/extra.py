# If-elif-else blokları:

# if-elif-else blokları karar yapıları olarak geçer.
# Yani şart durumlarını temsil eder. 
# if'in Türkçe karşılığı eğerdir. 
# Kullanım Amacı: Eğer bu koşul gerçekleşirse şunu yap gerçekleşmezse şunu yap diyebilmek için kullanılır.
# Programlamada en çok kullanılan bloklardandır.
# Düşünelim: Bir küvet düşünelim su sürekli açık kalsaydı ne olurdu? 

su_miktari = int(input("Su miktarını giriniz? (cm) "))
if su_miktari > 120:
    print("Su miktarı fazla. Tahliye sistemi devreye girsin")
else:
    print("Su normal seviyede")

# Karşılaştırma Operatörleri

# >  Büyüktür operatörü
# <  Büyüktür operatörü
# >= Büyük eşittir operatörü
# >= Küçük eşittir operatörü
# == Eşittir
# != Eşit değildir.
# %  Mod operatörü(Kalan bulma)

sayi = int(input("Sayınızı giriniz:")) 

if sayi > 0:
    print("Girilen sayı pozitiftir.")
elif sayi == 0:
    print("Girilen sayı nötrdür.(0)")
else:
    print("Girilen sayı negatiftir.")


kontrol_edilecek_numara = int(input("Kontrol edilecek numarayı giriniz: "))

if kontrol_edilecek_numara % 2 == 0:
    print("Çift Sayı")
else:
    print("Tek Sayı")

# Lunapark Trenine Giriş Şartları:
boy_uzunlugu = int(input("Boy uzunluğunuzu giriniz: (cm) "))
if boy_uzunlugu >= 120:
    yas = input("Yaşınızı giriniz: ")
    if yas <= 18:
        print("Bilet Fiyatınız 7$")
    else:
        print("Bilet Fiyatınız 12$")
else:
    print("Trene binemezsiniz.")


# Vücüt Kitle İndexi Hesaplama
kilo = 85
uzunluk = 1.85

vucut_kitle_indexi = kilo / (uzunluk * uzunluk)

if vucut_kitle_indexi < 18.5:
    print("Zayıf")
elif vucut_kitle_indexi < 25:
    print("Normal Kilolu")
else:
    print("Fazla kilolu")



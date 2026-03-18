# Araştırma sorusu (Gelecek Haftaya öğrenip gelimeleri için) pythonda en yakına yuvarlamak için hangi fonksiyon kullanılır? 
print(round(3.66))

#Ek Bilgiler
import math

sayi = 3.66

print(sayi // 1)        # 3.0
print(round(sayi))      # 4

print(math.ceil(sayi))  # 4
print(math.floor(sayi)) # 3

#Ek bilgi round fonksiyonu 2 paremetre alabilir.
#Bu paremetre kaç basamak yuvarlamak istediğimi söyleriz

print(round(sayi,1))    # 3.7



# Hesap Ödeme Tutarı Hesaplayıcı
print("Hesap Ödeme Ekranı Hoşgeldiniz!")

toplam_hesap_tutari = float(input("Toplam Hesap tutarınız? $"))
bahsis = int(input("Yüzde kaç bahşiş vermek istersiniz? %10, %12 veya %15? "))
toplam_kisi = int(input("Hesabı bölüşecek kişi sayısı kaçtır? "))

bahsis_miktari = (toplam_hesap_tutari * bahsis) / 100

hesap = round((toplam_hesap_tutari + bahsis_miktari) / toplam_kisi,2)

print(f"Kişi başına düşen miktar: {hesap:.2f}")
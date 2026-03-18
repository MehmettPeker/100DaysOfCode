# Hesap Ödeme Tutarı Hesaplayıcı
print("Hesap Ödeme Ekranı Hoşgeldiniz!")

toplam_hesap_tutari = float(input("Toplam Hesap tutarınız? $"))
bahsis = int(input("Yüzde kaç bahşiş vermek istersiniz? 10, 12 veya 15? %"))
toplam_kisi = int(input("Hesabı bölüşecek kişi sayısı kaçtır? "))

bahsis_miktari = (toplam_hesap_tutari * bahsis) / 100

hesap = round((toplam_hesap_tutari + bahsis_miktari) / toplam_kisi,2) #Hesap virgülden sonra 2 basamak olacak.

print(f"Kişi başına düşen miktar: ${hesap}") 

# Hesap Ödeme Tutarı Hesaplayıcı
print("Hesap Ödeme Ekranı Hoşgeldiniz!")

toplam_hesap_tutari = float(input("Toplam Hesap tutarınız? $"))
bahsis = int(input("Yüzde kaç bahşiş vermek istersiniz? %10, %12 veya %15? "))
toplam_kisi = int(input("Hesabı bölüşecek kişi sayısı kaçtır? "))


toplam = toplam_hesap_tutari * (1 + bahsis / 100)
hesap = round(toplam / toplam_kisi,2)
print(hesap)


#Ek Bilgi: 

sinav = [1,2,3,4]
print(type(sinav))  #list ==> Liste


sinav2 = {"İsim":"Ali","Soyisim":"Peker"}
print(type(sinav2)) #dict ==> Sözcük

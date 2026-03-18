#FORMATIF STRING

#Kullanım sebebi1: Farklı veri tiplerini birleştirmekte TypeError hatasından kurtulmak 

sayac = 0
# print("Sayac numarası"+sayac) #TypeError hatası
# Bu hatadan kurtulmak için formatif strin kullanılır.

#Kullanım sebebi2: Çok fazla değişken olduğunda onları birleştirmek için çok fazla + sembolü kullanmamız gerekir. Bu da okunaklığı ve kod temizliği açısından sıkıntı yaratabilir.

#Yazım Kuralı1: tırnaklardan önce f" " sembolü eklenir.
#Yazım Kuralı2: Formatif string değişkenler yazılırken tırnakların içine ve değişkenler {} içine yazılmalır.
print(f"Sayac numarası {sayac}" )




isim = "Mehmet"
soyisim = "Peker"
okul_no = 105
sinif = "12/A"

print("İsminiz: " + isim + " Soyisminiz: " + soyisim + " Okul Numaranız: " + str(okul_no) + " Sınıfınız: " + sinif)
# 7 Tane birleştirme sembolü kullandık buda programcının işlem yükünü artıyor.
# Genel olarak kısa işlemlerde + sembolü daha fazla birleştirme ve karışık yapılarda formatif string kullanılır.
print(f"İsminiz: {isim} Soyisminiz: {soyisim} Okul Numaranız: {okul_no} Sınıfınız: {sinif}")

#Formatif stringin Avantajları
# 1) Çok fazla + sembolü kullanmak zorunda kalmadık.
# 2) TypeError hatası almadık.
# 3) TypeError hatasında kurtulmak için dönüşüm yapmamıza gerek kalmadı.

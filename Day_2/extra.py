print("Hello"[0]) # ==> Dizinin ilk karekterini buluruz.

#String 

print("123"+"456")

#Integer 

print(123 + 456)

#Ek bilgi 
#Büyük sayıların daha okunaklı olması için tam sayıların arasına _ kullanılabilir.

print(123_456_789)


#Float 
#Ondalıklı sayıların veri tipine denir.
print(3.14159)

#Boolean

#Yanlızca iki seçeneği olan True ve False değerini alan veri tipidir.

print(True)
print(False)


#type fonksiyonu
#Verilen ifaden hangi veri tipine gösterir.

type("123") #str
type(123)   #int
type(True)  #bool
type(3.14)  #float

#Veri Dönüşümü
int("123") 
print("123"+"456")
print(int("123")+int("456"))
str(123)

#Matematiksel Operatörler

# Toplama (+)
# Çıkarma (-)
# Çarpma  (*)
# Bölme   (/)
# Kuvvetini alma (**)


print(10+20) #30 
print(30-10) #20
print(10*10) #100
print(20/10) #2.0 
print(2**3)  #8


#Ek Bilgi
print(5//3) #Yaptığı işlem ondalarıkları kaldırır.
#Python bölme işleminde net sonucu kullanıcıya 
#aktarmak için veri tipini float olarak ayarlar.
# Bu işlemi sadece bölme işlemi için yapar.
# Eğer biz tam sayı olarak görmek istersek
# virgül kullanmak istemezsek o zaman // kullanılır.
# Not: Eğer tam sayı bölünmesi olmazsa 
# mesala (10/3) verisinin sonucu 3.3333 
# Eğer // kullanırsak yuvarlama yaparken 
# 3 e yuvarlar. Sonuç 3.666 olsa bile 3 yuvarlama yapar.
# O yüzden // kullanılırken dikkatli olmak gerekir.
# Araştırma sorusu (Gelecek Haftaya öğrenip gelimeleri için) pythonda en yakına yuvarlamak için hangi fonksiyon kullanılır? 


# İŞLEM ÖNCELİĞİ

# 1. ()
# 2. **
# 3. * veya / ==> birilerine üstünlüğü yok ilk olarak solda ki işlem yapılır.
# 4. + veya - ==> birilerine üstünlüğü yok ilk olarak solda ki işlem yapılır.

print(3 * 3 + 3 / 3 -3) #Thonny göster
#Ekran çıktısı 7.0 oluyor.
 
#Soru => Eğer biz bunu 7 olarak göstermek isteseydik napardık?


#Artılı Soru ==> Vücut kitle indexi hesaplama.
# formül VKİ = kilonun boyun karesine bölümü
# Not kiloyu kg boyu metre cinsinden olacak.
# Çözüm exam_1.py de

# Arttırma Azaltma işlemi.

score = 0
score = score + 1 
print(score) #1
#Bir farklı gösterimi kısa yol
score += 1



#Azaltma işlemi
score1 = 1
score1 = score1 - 1
print(score1) #0
#Kısayolu
score1 -= 1


# Çarpma İşlemi
score2 = 2
score2 = score2 * 2
print(score2) #4
#Kısayolu
score *= 2


# Bölme İşlemi
score3 = 2
score3 = score3 / 2
print(score3) #1
#Kısayolu
score3 /= 2



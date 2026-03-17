#Değişkenler. 
# Verileri sakladığımız alanlardır. Hafızada tuttuğumuz verilerdir.
# Soru ==> Bilgisayarda ki veriler nerede saklanır?

input("What is your name ")
# Biz ismimizi girdikten sonra hiç bir ekran çıktısı göremedik bunun sebebi bu veriyi bir hafızada tutmadığımız içindir.

#Değişken tanımlayarak bu veriyi hafızada tutabiliriz.
#Düşünelim telefon numaraları kaydetmeden hayatımızı sürdürmemiz gerekseydi telefon rehberimizde 100 lerce numarayı hatırlayabilirmiydik? 
#Ama biz şu anda telefon numaralanın kime ait olduğunu kayıt eder kullanabiliyoruz. Değişkenlerde bunun için kullanılır. Veriyi hafızada tutmak için.
# ali = 0232 000 23 33 ==> Artık telefon numarasını bilmeden ali ismine ulaşarak telefon numarasına ulaşabilirim.
#Yukarıda ki örnekği şu şekilde yazarsak artık bilgisayar hafızasında tutabiliriz?
isim = input("What is your name")
print(isim)

#DEĞİKEN TANIMLAMA KURALLARI:

#1) Rakamla başlayamaz.
#1isim= "Jale"

#2) pythonda kullanılan fonksiyonlar değişken ismi olarak tanımlanamaz.
"""

input = "girdi"
print = "ekrana yazdırma"
print(input)
print(print)

"""
#3) ingilize karekter kullanmak önemlidir.
#şehir = "istanbul"  # yerine ==> sehir = "istanbul" ş yerine s harfini kullandık.

#4) Birden fazla kelimeden oluşuyorsa boşluk kullanmamaalıyız.
# isim soyisim = "Jale Yıldız" #yerine ==> isim_soyisim(Snackcase) veya isimSoyisim(Camelcase) şekilde değişken tanımlamalıyız. 

#<==== Üst seviye bir ek bilgi ====>
# pythonun zor konularından birisi olan class tanımlamları yapılırken ilk harfi büyük şekilde tanımlama yapılır. birden fazla kelimeden oluşyorsa O kelimelerinde baş harfi büyük yazılır.

#5) _(alt çizgi dışında sembol kullanılamaz.(>£#$$½§{[[]]]}\- vb. tüm temboller kullanılamaz.))
#sinif-okul = "12/A Kars Fen Lisesi" yerine alt satırdaki gibi tanımla yapılmalıdır.
sinif_okul = "12/A Kars Fen Lisesi"
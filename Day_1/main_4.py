
# Değişkenler
# Programlamada istediğimiz verileri depolamamıza yarayan yapılardır. 
# Genel olarak o veriyi tekrar tekrar kullanmak için kullanırız.

# Geneel Kültür Soru ==> Bilgisayarlarımızda ki depolama birimleri nelerdir?

input("What is your name ")
# Biz ismimizi girdikten sonra bu veriyi hafızada tutmadığımız için o veriye bir daha ulaşamayız.
# Eğer değişkenler olmasaydı internette ki hiçbir üyelik sistemine giriş yapamazdık.


# Yazdığımız programlarda değişken tanımlayarak bu veriyi hafızada tutabiliriz.

# Düşünelim telefon numaraları kaydetmeden hayatımızı sürdürmemiz gerekseydi nasıl olurdu? Telefon rehberimizde 100 lerce numarayı hatırlayabilirmiydik? 
# Ama biz şu anda telefon numaralanın kime ait olduğunu kayıt eder kullanabiliyoruz. Değişkenlerde bunun için kullanılır. Veriyi hafızada tutmak için.
# Ali = 0232 000 23 33 ==> Artık telefon numarasını bilmeden ali ismine ulaşarak telefon numarasına ulaşabilirim.

# Yukarıda ki örnekği şu şekilde yazarsak artık bilgisayar hafızasında tutabilirmiydik?
isim = input("What is your name")
print(isim)

                                            # DEĞİKEN TANIMLAMA KURALLARI: Not: Deneme tahtasında göster.

# 1) Rakamla başlayamaz.
# 1isim= "Jale"

# 2) pythonda kullanılan fonksiyonlar değişken ismi olarak tanımlanamaz.
"""

input = "girdi"
print = "ekrana yazdırma"
print(input)
print(print)

"""
# 3) İngilize karekter kullanmak çok önemlidir.
# şehir = "istanbul"  # yerine ==> sehir = "istanbul" ş yerine s harfini kullanmalıyız.

# 4) Birden fazla kelimeden oluşuyorsa boşluk kullanmamalıyız.
# isim soyisim = "Jale Yıldız" #yerine ==> isim_soyisim(snake_case) veya isimSoyisim(Camelcase) şekilde değişken tanımlamalıyız. 

# <==== Üst seviye bir ek bilgi ====>
# Pythonun zor konularından birisi olan class tanımlamaları yapılırken ilk harfi büyük şekilde tanımlama yapılır. Birden fazla kelimeden oluşyorsa O kelimelerinde baş harfi büyük yazılır. #PascalCase

# 5) _ (alt çizgi dışında sembol kullanılamaz. (> £ # $ ½ § { [ [ ] ] } \ - vb. tüm temboller kullanılamaz.)) Sadece _ kullanılır.
# sinif-okul = "12/A Kars Fen Lisesi" yerine alt satırdaki gibi tanımla yapılmalıdır. #Deneme tahtasında göster.
sinif_okul = "12/A Kars Fen Lisesi"
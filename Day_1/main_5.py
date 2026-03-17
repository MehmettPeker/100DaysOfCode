#Uzunluk hesaplama fonksiyonu => length bulma

#Bir verilen uzunluğunu bulmak istiyorsak len() fonksiyonu kullanır.
#Eğer len fonksiyonu kullanmadan uzunluk hesaplamak isteseydik şu şekilde yapardık.

isim = "Ali"
sayac= 0
bos_liste= []
for i in isim:
    bos_liste.append(i)
    sayac += 1
print(sayac)

uzunluk = len(isim)
print(uzunluk)


#Soru ==> Kullanıcıdan kullanıcı adını alınız daha sonra bu kullanıcı adının kaç karekterden oluştuğunu bulunuz? (Artılı Soru)
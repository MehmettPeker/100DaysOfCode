Bugün Ne Öğrendim:
1) if-else bloklarını öğrendim.
2) Akış diyagramı tasarlayabileceğim bir site öğrendim.(url'ye ==> draw.io yaz.)






10 ) Python’da bir koşulda and ve or birlikte kullanılıyorsa, Python önce and kısmını değerlendirir. Bu yüzden parantez kullanılmazsa sonuç beklediğimizden farklı çıkabilir. Karışıklığı önlemek ve kodu daha anlaşılır yapmak için böyle durumlarda parantez kullanmak en güvenli yoldur.

ÖRNEĞİN:

if yas > 18 and ogrenci_mi or calisiyor_mu:
    print("Uygun")

Python bunu şöyle değerlendirir:
if (yas > 18 and ogrenci_mi) or calisiyor_mu:
    print("Uygun")

Yani kişi çalışıyorsa, diğer şartlara bakmadan koşul doğru olabilir.
Daha açık ve güvenli yazım:

if yas > 18 and (ogrenci_mi or calisiyor_mu):
    print("Uygun")
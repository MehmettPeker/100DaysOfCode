print("Python Pizza'ya Hoşgeldiniz")

pizza_boyutu = input("Pizzanız hangi boyutta olsun? S, M veya L: ")
ozel_sos = input("Özel sos ister misiniz? Y veya N: ")
extra_peynir = input("Extra peynir ister misiniz? Y veya N: ")

pizza_fiyati = 0

if pizza_boyutu == "S":
    pizza_fiyati = 15
elif pizza_boyutu == "M":
    pizza_fiyati = 20
elif pizza_boyutu == "L":
    pizza_fiyati = 25

if ozel_sos == "Y":
    if pizza_boyutu == "S":
        pizza_fiyati += 2
    else:
        pizza_fiyati += 3

if extra_peynir == "Y":
    pizza_fiyati += 1

print("Toplam hesap $" + str(pizza_fiyati))
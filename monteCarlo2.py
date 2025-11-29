import random

def bir_oyun_tipi(tip):
    p1 = 100
    p2 = 100
    kasa = 0
    oyun_ucreti = 10

    while p1 >= 3 and p2 >= 3:
        x = random.random()

        if tip == 1:
            if x < 0.2:
                p1 += oyun_ucreti * 0.9
                kasa += oyun_ucreti * 0.1
                p2 -= oyun_ucreti * 0.9
            elif x < 0.9:
                p2 += oyun_ucreti * 0.9
                kasa += oyun_ucreti * 0.1
                p1 -= oyun_ucreti * 0.9
            else:
                pass

        else:
            if x < 0.4:
                p1 += oyun_ucreti * 0.9
                kasa += oyun_ucreti * 0.1
                p2 -= oyun_ucreti * 0.9
            elif x < 0.8:
                p2 += oyun_ucreti * 0.9
                kasa += oyun_ucreti * 0.1
                p1 -= oyun_ucreti * 0.9
            else:
                pass

    return kasa

def monte_carlo(sim_sayisi, tip):
    toplam = 0
    for _ in range(sim_sayisi):
        toplam += bir_oyun_tipi(tip)
    return toplam / sim_sayisi

print("Tip 1 ortalama kasa:", monte_carlo(1000, 1))
print("Tip 2 ortalama kasa:", monte_carlo(1000, 2))
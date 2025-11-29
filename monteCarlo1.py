import random

def otomotik(kere):
    kırmızı = 0
    mavi = 0

    for i in range(kere):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1:
            kırmızı += 1
        else:
            mavi += 1
    sonuc = kırmızı / mavi
    print(kırmızı)
    print(mavi)
    return (sonuc)
print(otomotik(10000))
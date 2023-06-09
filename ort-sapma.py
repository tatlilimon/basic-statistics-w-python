GREEN = '\033[92m'
END = '\033[0m'
def ortalama_sapma(veri_seti):
    toplam = 0
    n = len(veri_seti)
    ortalama = sum(veri_seti) / n

    for veri in veri_seti:
        toplam += abs(veri - ortalama)

    ortalama_sapma = toplam / n
    return ortalama_sapma

# Verisetini, veri adlı diziye yerleştir.
veri = [23,34,37,45,50,56,57,70,77,86,91]
sonuc = ortalama_sapma(veri)
print(GREEN +"Ortalama Sapma:" + END, sonuc)

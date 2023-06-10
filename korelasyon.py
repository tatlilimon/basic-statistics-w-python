import numpy as np
from colorama import Fore, Style

# Kullanıcıdan veri setlerini girmesini iste
input_data1 = input(Fore.BLUE + "1. veri grubunuzun elemanlarını; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
input_data2 = input(Fore.BLUE + "2. veri grubunuzun elemanlarını; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)

# Kullanıcının girdiği veriyi virgülle böl ve numpy dizisine dönüştür
data1 = np.array([float(x) for x in input_data1.split(",")])
data2 = np.array([float(x) for x in input_data2.split(",")])

# Korelasyon katsayısının hesaplama kısmı
correlation_matrix = np.corrcoef(data1, data2)

# Korelasyon katsayısı, korelasyon matrisinin dış köşegenlerinde yer alır
correlation_coefficient = correlation_matrix[0, 1]

print(Fore.GREEN + "Korelasyon katsayısı: " + Fore.RESET, correlation_coefficient)

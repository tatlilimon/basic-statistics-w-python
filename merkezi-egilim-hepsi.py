import numpy as np
from scipy import stats
from colorama import Fore, Style

def calculate_statistics(data):
    # Aritmetik ortalama bulmak için
    mean = np.mean(data)
    print(Fore.GREEN +"Aritmetik Ortalama: " + Fore.RESET, mean)

    # Medyan bulmak için
    median = np.median(data)
    print(Fore.GREEN +"Medyan: " + Fore.RESET, median)

    # Mod bulmak için
    mode = stats.mode(data)
    print(Fore.GREEN +"Mod: " + Fore.RESET, mode[0][0])

    # Çeyrek değerler bulmak için
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    print(Fore.GREEN +"Q1: " + Fore.RESET, q1)
    print(Fore.GREEN +"Q3: " + Fore.RESET, q3)

    # Standart sapma bulmak için
    std_dev = np.std(data)
    print(Fore.GREEN +"Standart Sapma: " + Fore.RESET, std_dev)

    # Varyans bulmak için
    variance = np.var(data)
    print(Fore.GREEN + "Varyans: " + Fore.RESET, variance)

print(Fore.BLUE + "Veri setinizi; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız" + Fore.RESET)
user_input = input()

# Kullanıcıdan alınan giriş virgülle ayrılır ve numpy arrayine dönüştürülür
data = np.array([float(i) for i in user_input.split(',')])

calculate_statistics(data)

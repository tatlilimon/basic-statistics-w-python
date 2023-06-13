import numpy as np
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()
# Kullanıcıdan veri setini girmesini iste
input_data = input(Fore.BLUE +"Veri setinizi; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
# Kullanıcının girdiği veriyi virgülle böl ve numpy dizisine dönüştür
data = np.array([float(x) for x in input_data.split(",")])

# Kullanıcıdan güven seviyesini girmesini iste
confidence_level = float(input(Fore.BLUE +"Güven seviyesini belirtiniz (0.05 yada 0.01): " + Fore.RESET))

# Güven seviyesine göre z skorunu belirle
z_score = 1.96 if confidence_level == 0.05 else 2.58 if confidence_level == 0.01 else None
if z_score is None:
    print(Fore.RED + "Geçerli bir güven seviyesi girilmedi!" + Fore.RESET)
    exit()

# Verinin ortalamasını hesapla
mean = np.mean(data)

# Standart hatayı hesapla
standard_error = 1 / np.sqrt(len(data))

print(Fore.GREEN +"Standart hata: " + Fore.RESET, standard_error)

# Güven aralığını hesapla
confidence_interval = mean - z_score * standard_error, mean + z_score * standard_error

print(Fore.GREEN +f"%{confidence_level*100} güven aralığı: " + Fore.RESET, confidence_interval)

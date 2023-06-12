from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

def mean_deviation(data_set):
    total = 0
    n = len(data_set)
    mean = sum(data_set) / n

    for data in data_set:
        total += abs(data - mean)

    mean_deviation = total / n
    return mean_deviation

# Kullanıcıdan veri sati alınır
input_data = input(Fore.BLUE + "veri grubunu; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
# Kullanıcıdan alınan giriş, virgülle ayrılır ve numpy arrayine dönüştürülür
data = [float(x) for x in input_data.split(",")]

result = mean_deviation(data)
print(Fore.GREEN +"Ortalama Sapma:" + Fore.RESET, result)

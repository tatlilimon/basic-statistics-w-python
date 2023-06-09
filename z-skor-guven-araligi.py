import numpy as np
GREEN = '\033[92m'
END = '\033[0m'
# Veri seti oluştur: 1,2,3,4 yazan kısıma veri setini giriniz.
data = np.array([1,2,3,4])

# Verinin ortalamasını hesaplanır
mean = np.mean(data)

# Standart hata hesaplanır
standard_error = (len(data) / np.sqrt(10))/10

print(GREEN +"Standart hata: " + END, standard_error)

# 95% güven aralığı hesaplama: Eğer 0.05 değil de 0.01 güven seviyesi isteniyorsa 1.96 yazan yerler 2.58 olarak değiştiriniz.
confidence_interval = mean - 1.96 * standard_error, mean + 1.96 * standard_error

print(GREEN +"%95 güven aralığı: " + END, confidence_interval)

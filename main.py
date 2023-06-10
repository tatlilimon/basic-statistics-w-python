import subprocess
from colorama import Fore, Style

def menu():
    print("************************************************************************************************")
    print(Fore.CYAN + "İstediğiniz Hesaplamayı Yapmak için İlgili Rakamı Girip Enterlayın " + Fore.RESET)
    print(Fore.GREEN + "[1]-> Merkezi Eğilim Ölçüleri Hesaplayıcısı(Mod,Medyan,Aritmetik ve Standart Sapma vb.)" + Fore.RESET)
    print(Fore.BLUE + "[2]-> Ortalama Sapma Hesaplayıcısı" + Fore.RESET)
    print(Fore.MAGENTA + "[3]-> Z-Skor Değeri ve Güven Aralığı Hesaplayıcısı" + Fore.RESET)
    print(Fore.RED + "[4]-> Normal T-Testi Değeri ve Güven Aralığı Hesaplayıcısı (iki grup birbirine bağlı değil ise)" + Fore.RESET)
    print(Fore.LIGHTRED_EX + "[5]-> Eşlenik T-Testi Değeri ve Güven Aralığı Hesaplayıcısı" + Fore.RESET)
    print(Fore.YELLOW + "[6]-> Ki-Kare Testi Hesaplayıcısı" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "[7]-> Ki-Kare Bağımsızlık Testi Hesaplayıcısı" + Fore.RESET)
    print(Fore.WHITE + "[8]-> F-Testi (ANOVA) Hesaplayıcısı" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "[9]-> Korelasyon Hesaplayıcısı" + Fore.RESET)
    print(Fore.WHITE + "[0]-> Çıkış" + Fore.RESET)

while True:
    menu()
    selection = input(Fore.CYAN + "Bir seçim yapınız: " + Fore.RESET)

    if selection == "1":
        subprocess.run(["python", "merkezi-egilim-hepsi.py"], check=True)
    elif selection == "2":
        subprocess.run(["python", "ort-sapma.py"])
    elif selection == "3":
        subprocess.run(["python", "z-skor-guven-araligi.py"])
    elif selection == "4":
        subprocess.run(["python", "normal-t-guven-araligi.py"])    
    elif selection == "5":
        subprocess.run(["python", "eslenik-t-guven-araligi.py"])    
    elif selection == "6":
        subprocess.run(["python", "ki-kare.py"])    
    elif selection == "7":
        subprocess.run(["python", "ki-kare-bagimsizlik.py"])    
    elif selection == "8":
        subprocess.run(["python", "f-testi.py"])    
    elif selection == "9":
        subprocess.run(["python", "korelasyon.py"])    
    elif selection == "0":
        break
    else:
        print("************************************************************************************************")
        print(Fore.RED + "Geçerli bir seçim yapınız! Doğru seçim, komut satırına sadece RAKAM girilip enter'a basılması ile olur." + Fore.RESET)

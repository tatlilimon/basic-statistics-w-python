import numpy as np
from scipy import stats
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

def calculate_statistics(data):
    mean = np.mean(data)
    print(Fore.GREEN +"Arithmetic mean: " + Fore.RESET, mean)

    median = np.median(data)
    print(Fore.GREEN +"Median: " + Fore.RESET, median)

    mode = stats.mode(data)
    print(Fore.GREEN +"Mod: " + Fore.RESET, mode[0][0])

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    print(Fore.GREEN +"Q1: " + Fore.RESET, q1)
    print(Fore.GREEN +"Q3: " + Fore.RESET, q3)

    std_dev = np.std(data)
    print(Fore.GREEN +"Standart deviatio: " + Fore.RESET, std_dev)

    variance = np.var(data)
    print(Fore.GREEN + "Variance: " + Fore.RESET, variance)

print(Fore.BLUE + "Enter your data set with commas between them" + Fore.RESET)
user_input = input()

data = np.array([float(i) for i in user_input.split(',')])

calculate_statistics(data)

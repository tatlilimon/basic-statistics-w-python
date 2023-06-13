import numpy as np
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

input_data = input(Fore.BLUE +"Enter your data set with commas between them: " + Fore.RESET)
data = np.array([float(x) for x in input_data.split(",")])

confidence_level = float(input(Fore.BLUE +"Enter the confidence level (0.05 or 0.01): " + Fore.RESET))

z_score = 1.96 if confidence_level == 0.05 else 2.58 if confidence_level == 0.01 else None
if z_score is None:
    print(Fore.RED + "Please enter valid confidence level" + Fore.RESET)
    exit()

mean = np.mean(data)

standard_error = 1 / np.sqrt(len(data))

print(Fore.GREEN +"Standart error: " + Fore.RESET, standard_error)

confidence_interval = mean - z_score * standard_error, mean + z_score * standard_error

print(Fore.GREEN +f"%{confidence_level*100} Confidence level: " + Fore.RESET, confidence_interval)

import numpy as np
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

input_data1 = input(Fore.BLUE + "Enter the 1st group's data set with commas between them " + Fore.RESET)
input_data2 = input(Fore.BLUE + "Enter the 2nd group's data set with commas between them " + Fore.RESET)

data1 = np.array([float(x) for x in input_data1.split(",")])
data2 = np.array([float(x) for x in input_data2.split(",")])

correlation_matrix = np.corrcoef(data1, data2)

correlation_coefficient = correlation_matrix[0, 1]

print(Fore.GREEN + "Correlation coefficient: " + Fore.RESET, correlation_coefficient)

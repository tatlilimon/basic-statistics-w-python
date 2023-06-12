import numpy as np
from scipy import stats
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

input_data1 = input(Fore.BLUE + "Enter the 1st group's data set with commas between them: " + Fore.RESET)
input_data2 = input(Fore.BLUE + "Enter the 2nd group's data set with commas between them: " + Fore.RESET)

sample1 = np.array([float(x) for x in input_data1.split(",")])
sample2 = np.array([float(x) for x in input_data2.split(",")])

confidence_level_input = float(input(Fore.BLUE + "Enter the confidence level (0.05 or 0.01): " + Fore.RESET))
confidence_level = 0.95 if confidence_level_input == 0.05 else 0.99 if confidence_level_input == 0.01 else None

if confidence_level is None:
    print(Fore.RED + "Please enter valid confidence level" + Fore.RESET)
    exit()

t_statistic, p_value = stats.ttest_ind(sample1, sample2)

degrees_freedom = len(sample1) + len(sample2) - 2
standard_error_difference = np.sqrt(np.var(sample1)/len(sample1) + np.var(sample2)/len(sample2))

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=np.mean(sample1)-np.mean(sample2), scale=standard_error_difference)

print(Fore.GREEN +"T statistics: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P value: " + Fore.RESET, p_value)
print(Fore.GREEN +"Confidence level: " + Fore.RESET, confidence_interval)

import numpy as np
from scipy import stats
from colorama import Fore, Style

paired_sample1_data = input(Fore.BLUE + "Enter the 1st group's data set with commas between them: " + Fore.RESET)
paired_sample1 = np.array([float(x) for x in paired_sample1_data.split(",")])
paired_sample2_data = input(Fore.BLUE + "Enter the 2nd group's data set with commas between them: " + Fore.RESET)
paired_sample2 = np.array([float(x) for x in paired_sample2_data.split(",")])

confidence_level_input = float(input(Fore.BLUE + "Enter the confidence level (0.05 or 0.01): " + Fore.RESET))
confidence_level = 0.95 if confidence_level_input == 0.05 else 0.99 if confidence_level_input == 0.01 else None

if confidence_level is None:
    print(Fore.RED + "Please enter valid confidence level" + Fore.RESET)
    exit()

t_statistic, p_value = stats.ttest_rel(paired_sample1, paired_sample2)

degrees_freedom = len(paired_sample1) - 1
mean_difference = np.mean(paired_sample1 - paired_sample2)
standard_error_difference = np.std(paired_sample1 - paired_sample2, ddof=1) / np.sqrt(len(paired_sample1))
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean_difference, scale=standard_error_difference)

print(Fore.GREEN +"T statistics: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P value: " + Fore.RESET, p_value)
print(Fore.GREEN +"Confidence level: " + Fore.RESET, confidence_interval)

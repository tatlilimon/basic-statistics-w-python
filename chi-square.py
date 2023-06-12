import numpy as np
from scipy.stats import chisquare
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

input_data = input(Fore.BLUE + "Enter your data set with commas between them: " + Fore.RESET)
observed_frequencies = np.array([float(x) for x in input_data.split(",")])

expected_frequencies = np.full_like(observed_frequencies, np.mean(observed_frequencies))

chi2_stat, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)

print(Fore.GREEN +"Chi-Square statistics: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"P value: " + Fore.RESET, p_val)
print(Fore.MAGENTA +"If Hypothesis Testing is to be done; after calculating the chi-square statistic value, open the following link in your browser" + Fore.RESET)
print(Fore.BLUE +"https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html" + Fore.RESET)
print(Fore.MAGENTA +"v=(total number of data-1), Red field=0.05 if the question asks for 0.01, type 0.01 and it will give you the x value. if the x value is greater than the chi-square statistic value, h0 is rejected. if it is smaller, h0 is accepted." + Fore.RESET)


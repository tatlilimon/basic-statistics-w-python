import numpy as np
from scipy.stats import f_oneway
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

num_groups = int(input(Fore.BLUE + "How many groups are in your dataset?: " + Fore.RESET))

groups = []
for i in range(num_groups):
    group_data = input(Fore.BLUE + f" Enter the data of the {i+1}.group with commas between them: " + Fore.RESET)
    groups.append(np.array([float(x) for x in group_data.split(",")]))

F, p = f_oneway(*groups)

print(Fore.GREEN +"F statistics: " + Fore.RESET, F)
print(Fore.GREEN +"P value: " + Fore.RESET, p)

print(Fore.MAGENTA +"To calculate the critical value, open the link below in your browser! " + Fore.RESET)
print(Fore.BLUE +"https://www.danielsoper.com/statcalc/calculator.aspx?id=4" + Fore.RESET)
print(Fore.MAGENTA +"Degrees of freedom is 1: (total number of groups-1)" + Fore.RESET)
print(Fore.MAGENTA +"Degrees of freedom 2: (total number of data in all groups - number of groups)" + Fore.RESET)
print(Fore.MAGENTA +"If the F statistic value is greater than the critical value, h0 is rejected, if it is smaller, it is accepted." + Fore.RESET)

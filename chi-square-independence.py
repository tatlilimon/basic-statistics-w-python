import numpy as np
from scipy.stats import chi2_contingency
from colorama import Fore, Style

num_rows = int(input(Fore.BLUE + "How many rows does your data set have: " + Fore.RESET))

observed_frequencies = []
for i in range(num_rows):
    row_data = input(Fore.BLUE + f"Enter the data of the {i+1}.row with commas between them: " + Fore.RESET)
    observed_frequencies.append([float(x) for x in row_data.split(",")])

observed_frequencies = np.array(observed_frequencies)

chi2_stat, p_val, dof, expected_frequencies = chi2_contingency(observed_frequencies)

print(Fore.GREEN +"Chi-Square statistics: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"P value: " + Fore.RESET, p_val)
print(Fore.GREEN +"Degrees of freedom: " + Fore.RESET, dof)
print(Fore.MAGENTA +"If Hypothesis Testing is to be done; after calculating the chi-square statistic value, open the following link in your browser" + Fore.RESET)
print(Fore.BLUE +"https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html" + Fore.RESET)
print(Fore.MAGENTA +"v=(rowNumber-1)*(columnNumber-1), Red field=0.05 if the question asks for 0.01, type 0.01 and it will give you the x value. if the x value is greater than the chi-square statistic value, h0 is rejected. if it is smaller, h0 is accepted." + Fore.RESET)

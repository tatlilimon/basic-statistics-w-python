from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

def mean_deviation(data_set):
    total = 0
    n = len(data_set)
    mean = sum(data_set) / n

    for data in data_set:
        total += abs(data - mean)

    mean_deviation = total / n
    return mean_deviation

input_data = input(Fore.BLUE + "Enter your data set with commas between them " + Fore.RESET)
data = [float(x) for x in input_data.split(",")]

result = mean_deviation(data)
print(Fore.GREEN +"average deviation:" + Fore.RESET, result)

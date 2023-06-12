import subprocess
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

def menu():
    print("************************************************************************************************")
    print(Fore.CYAN + "Enter the Relevant Number and Enter to Make the Calculation You Want " + Fore.RESET)
    print(Fore.GREEN + "[1]-> Central Tandency Calculator" + Fore.RESET)
    print(Fore.BLUE + "[2]-> Average Deviation Calculator" + Fore.RESET)
    print(Fore.MAGENTA + "[3]-> Z-Score Confidence Level Calculator" + Fore.RESET)
    print(Fore.RED + "[4]-> Normal T-Test Value and Confidence Level Calculator" + Fore.RESET)
    print(Fore.LIGHTRED_EX + "[5]-> Paired T-Test Value and Confidence Level Calculator" + Fore.RESET)
    print(Fore.YELLOW + "[6]-> Chi-Square Test Calculator" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "[7]-> Chi-Square Independence Test Calculator" + Fore.RESET)
    print(Fore.WHITE + "[8]-> F-Test (ANOVA) Calculator" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "[9]-> Correlation Coefficient Calculator" + Fore.RESET)
    print(Fore.WHITE + "[0]-> Exit!" + Fore.RESET)

while True:
    menu()
    selection = input(Fore.CYAN + "Choose one of the tools: " + Fore.RESET)

    if selection == "1":
        subprocess.run(["python", "central-tendency.py"], check=True)
    elif selection == "2":
        subprocess.run(["python", "average-deviation.py"])
    elif selection == "3":
        subprocess.run(["python", "z-score-confidence-level.py"])
    elif selection == "4":
        subprocess.run(["python", "normal-t-confidence-level.py"])    
    elif selection == "5":
        subprocess.run(["python", "paired-t-confidence-level.py"])    
    elif selection == "6":
        subprocess.run(["python", "chi-square.py"])    
    elif selection == "7":
        subprocess.run(["python", "chi-square-independence.py"])    
    elif selection == "8":
        subprocess.run(["python", "f-test.py"])    
    elif selection == "9":
        subprocess.run(["python", "correlation-coefficient.py"])    
    elif selection == "0":
        break
    else:
        print("************************************************************************************************")
        print(Fore.RED + "Make a valid selection! The correct choice is made by simply entering the NUMBER on the command line and pressing enter." + Fore.RESET)

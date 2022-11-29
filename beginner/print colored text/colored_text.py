import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset = True)

print(Fore.BLUE + Back.YELLOW + "Hi, my name is Zulfikar Muhamad " + Fore.YELLOW + Back.BLUE + "I love Python")
print(Back.CYAN + "Hi, my name is Zulfikar Muhamad")
print(Fore.RED + Back.GREEN + "Hi, my name is Zulfikar Muhamad")
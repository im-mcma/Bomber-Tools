# import requests as req
from os import path, system


if path.exists("./requirements.txt"):
    with open("./requirements.txt") as file:
        libs = [i.split("==")[0] for i in file.readlines()]
    
    for lib in libs:
        print(lib)
        try:
            __import__(lib)
        except ModuleNotFoundError:
            system("pip install "+lib)


from pystyle import Col, Center, System
from Plugins.api_list import handler
from colorama import Fore
from Plugins.functions import Functions

r, g = Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX

if __name__ == "__main__":
    logo = f"""
{Fore.YELLOW}╭──────────── 🔹 Tool Information 🔹 ────────────╮{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}                                                {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}  {Fore.RED}Tool Name:{Fore.RESET} Bomber Tools                       {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}  {Fore.CYAN}Channel:{Fore.RESET} KartBankiHack                        {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}  {Fore.GREEN}Link:{Fore.RESET} https://t.me/chalder_OTP              {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}  {Fore.MAGENTA}Created by:{Fore.RESET} 𝕚𝕞_𝕒𝕓𝕚                            {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}│{Fore.RESET}                                                {Fore.YELLOW}│{Fore.RESET}
{Fore.YELLOW}╰────────────────────────────────────────────────╯{Fore.RESET}
"""

if __name__ == "__main__":
    # باز کردن لینک تلگرام هنگام اجرای کد
    system("xdg-open tg://resolve?domain=halder_OTP")  
 



    while True:
        System.Clear()
        print(Center.XCenter(logo))

        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call(off)",
                "2": "sms"
            }
            print(f"{Col.yellow}[!]{Col.gray} Proxies are {proxy_state}")
            print(f"{Col.yellow}[!]{Fore.CYAN} Choices: ")

            for ch in choices:
                print(f"   {Fore.CYAN}{ch}- {Fore.GREEN}{choices[ch].capitalize()} Bomber ")
            
            print()
            choice = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter Your Choice: {Col.green}", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter the phone number {Fore.CYAN}[9xxxxxxxxx]{Col.gray}: {Col.green}", checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)
            count = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter spam count: {Col.green}", lambda x: x.isnumeric() and int(x) >= 0)

            Functions.start(choices[choice], number, int(count))


        except KeyboardInterrupt:
            print("\n" + Fore.BLUE, "Exiting...")
            exit()

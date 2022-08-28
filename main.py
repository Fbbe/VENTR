import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import ctypes
import string
import os
import time

USE_WEBHOOK = True

os.system('cls' if os.name == 'nt' else 'clear')


try:  
    from discord_webhook import DiscordWebhook  
except ImportError:  
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  
try:  
    import numpy  
except ImportError:  
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  
try:  
    import colorama 
except ImportError:  
    input(
        f"Module colorama not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install colorama'\nPress enter to exit")
    exit()  

class NitroGen:  
    def __init__(self):  
        self.fileName = "Valid Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "VENTR by Fab#7542")  
        else:  
            print(f'\33]0;VENTR by Fab#7542\a',
                  end='', flush=True)  

        print(Fore.GREEN + """             _/      _/  _/_/_/_/  _/      _/  _/_/_/_/_/  _/_/_/    
            _/      _/  _/        _/_/    _/      _/      _/    _/   
           _/      _/  _/_/_/    _/  _/  _/      _/      _/_/_/      
            _/  _/    _/        _/    _/_/      _/      _/    _/     
             _/      _/_/_/_/  _/      _/      _/      _/    _/ 
                                                        """)  
        time.sleep(2)  
        
        self.slowType(
            "\nInput amount you wish to generate and check: ", .02, newLine=False)

        try:
            num = int(input(''))  
        except ValueError:
            input("Input needs to be a number.\nPress enter to exit")
            exit()  

        if USE_WEBHOOK:
            self.slowType(
                "[OPTIONAL] Enter Discord webhook or press enter to proceed anyways: ", .02, newLine=False)
            url = input('')  
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f">> VENTR has started\nAny valid codes will be sent here"
                    ).execute()


        valid = []  
        bad = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result:  
                    valid.append(url)
                else:  
                    bad += 1 
            except KeyboardInterrupt:
                print("\nUser Interruption Occurred")
                break  

            except Exception as e:  
                print(f" Failed - {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Software made - {len(valid)} Valid | {bad} Bad - by Fab#7542")  
                print("")
            else:  
                print(
                    f'\33]0;Software made - {len(valid)} Valid | {bad} Bad - by Fab#7542\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Bad: {bad}
 Valid Codes: {', '.join(valid)}""")  

        input("\nDone! Press enter 3 times to close the program.")
        [input(i) for i in range(2, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200:  
            print(Fore.GREEN + f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"a Valid Nitro Code was Found! \n{nitro}"
                ).execute()

            return True  

        else:
            print(Fore.RED + f" Bad | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  

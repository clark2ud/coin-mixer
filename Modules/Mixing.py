import sys
import os
from Menu import *
from Print import *
import time
class CoinMixer:
    def CoinMixer():
        a = cprintinput("Amount to Mix: ", "y", True)
        netloss = "10-15%"
        cprint(f"Expected net loss: {netloss}", "y", True)
        print()

        TargetWallet = CryptoWallets.RetriveTargetWallet()
        cprint(f"Current Target Wallet -> {TargetWallet}", "g", True)
        print(Fore.RED + "Once started. mixing cannot be interrupted or undone!\nMistakes will be expensive!")
        
        choice = cprintinput("Are you sure You want to Mix? (y/n): ", "y", True)
        if choice == "y":
            os.sys("clear")
            InitalizeBackground()
            
            # implementation goes here later...

        if choice == "n":
            os.sys("clear")
            InitalizeBackground()
            cprint("Enjoy money laundering!", "y", True)
            time.sleep(1)
            cprint("Bye!", "r", False)
            time.sleep(1)
            exit()
import sys
import os
from Menu import *
from Print import *
import time
import random
import string
class CoinMixer:
    def GetRandomCryptoWallet():
            addr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
            crypto = random.choice(["btc", "ltc", "eth"])
            join  = crypto + addr
            return join
    def CoinMixer():
        a = cprintinput("Amount to Mix: ", "y", True)
        netloss = "10-15%"
        cprint(f"Expected net loss: {netloss}", "y", True)
        print()

        PhysicalWallet = CryptoWallets.RetrivePhysicalWallet()
        cprint(f"Current Physical Wallet -> {PhysicalWallet}", "g", True)
        print(Fore.RED + "Once started. mixing cannot be interrupted or undone!\nMistakes will be expensive!")
        
        choice = cprintinput("Are you sure You want to Mix? (y/n): ", "y", True)
        if choice == "y":
            os.sys("clear")
            InitalizeBackground()
            for i in range(16):
                cprint(GetRandomCryptoWallet()[:20], "g", False)
                time.sleep(random.uniform(0.1, 3))

            
            # implementation goes here later...

        if choice == "n":
            os.sys("clear")
            InitalizeBackground()
            cprint("Enjoy money laundering!", "y", True)
            time.sleep(1)
            cprint("Bye!", "r", False)
            time.sleep(1)
            exit()
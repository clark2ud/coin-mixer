import sys
import os
from Menu import *
from Print import *
import time
class CoinMixer:
    def CoinMixer():
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
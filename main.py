from Modules.Menu import *
from Module.Print import *
import ctypes

def main():
    # add requirements here later!
    ctypes.windll.kernel32.SetConsoleTitleW("Made By @clark2ud")
    InitializeBackground()
    InitlializeMenu()
main()
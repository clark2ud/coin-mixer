import shutil
import time
import sys
import math
from colorama import Fore, Back, Style
from Wallets import CryptoWallets
from Mixing import CoinMixer
class Menu:
    def InitializeLogo(background=None, max_width=20):

            logo = """
            ⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣶⣦⣤⣤⣀⠀⠀
    ⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶
    ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣠⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⠟⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠿⠿⠿⢻⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⠀⠀⠀⢀⣴⡾⠿⠛⠛⠻⣷⣄⠀⠀⠀⠀⢠⣾⠛⠉⠉⠉⠻⣆⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠀⠀⠀⠀⠀⢰⣿⠋⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢀⡿⠃⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣇⣠⣤⣤⣤⣠⡇⠀⠀⠀⠀⠀⠀⠀⢠⣟⣀⣠⣤⣀⣿⡆⠀⠀⠀⠀⠀⠀⠀⢸⣷⣤⣷⣦⣀⠀⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠋⠉⠙⢿⡇⠀⠀⠀⠀⠀⠀⢠⣿⣛⣭⣤⣤⣬⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⠀⠈⠻⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟⠛⠻⢿⣿⡏⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⡿⠿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⢹⣿⣿⠟⠛⠛⠿⣷⣦⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀⠀⣾⠁⠀⠘⣿⣿⣿⣿⣿⡟⠉⢷⡀⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠈⢻⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⢹⣿⣿⣿⣿⡇⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠻⣿⣶⣶⣾⣿⠗⠂⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠀⠀⠈⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣽⣿⣿⣧⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣀⣤⣤⣤⠶⠞⠁⠀⠀⠀⠀⠀⣿⡏⠉⢻⡶⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠁⠈⢿⣆⠀⠀⠀⠉⠛⠈⠛⠛⠛⠶⠶⠶⠶⢤⣄⣾⠃⠀⠀⠀⠸⣿⡀⠈⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠈⣻⣦⣀⠀⣿⡂⢠⡶⣂⣀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠙⣷⣄⠀⠀⠀⢰⣖⣿⣐⠿⠆⠀⢀⣀⣤⣾⡋⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⢰⡟⠀⠙⠋⠀⠀⢻⣀⣛⣁⣀⣀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣤⠤⠭⠤⠤⠀⠀⠘⠛⠉⠉⣿⢇⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣜⢿⣦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⣹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣯⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⣿⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣿⣿⣿⣶⣦⣤⣤⣤⣤⣴⠾⣿⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣿⠻⢷⣶⣶⣴⣶⣶⣾⣿⣿⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢿⡿⠛⠛⢻⣿⠟⠛⠛⠛⢿⠃⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⡀⠈⠳⣤⣀⣉⣁⣀⣀⣠⡴⠇⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⠳⢦⣽⣄⠀⠈⠉⠉⠉⠉⠉⠁⠀⢀⣴⣤⡶⠟⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠈⠙⢿⣶⣶⣶⣶⣶⣶⣶⣶⠟⠉⠁⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢿⣿⡿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """

            source = [line.strip(" ") for line in logo.splitlines()]
            source = [line for line in source if line]
            source_width = max(len(line) for line in source)
            source = [line.ljust(source_width) for line in source]

            terminal_width = shutil.get_terminal_size((80, 24)).columns
            canvas_width = max(1, min(max_width, terminal_width - 2))
            output_width = min(source_width, canvas_width)
            output_height = max(1, round(len(source) * output_width / source_width))

            scaled = []
            for y in range(output_height):
                source_y = min(len(source) - 1, y * len(source) // output_height)
                row = []
                for x in range(output_width):
                    source_x = min(source_width - 1, x * source_width // output_width)
                    row.append(source[source_y][source_x])
                scaled.append(row)

            if isinstance(background, str):
                background_lines = background.splitlines()
            else:
                background_lines = list(background) if background is not None else []
            canvas_width = max(canvas_width, max(
                (len(line) for line in background_lines), default=0
            ))
            canvas_height = max(len(background_lines), output_height)
            canvas = [
                list(background_lines[y].ljust(canvas_width))
                if y < len(background_lines) else [" "] * canvas_width
                for y in range(canvas_height)
            ]

            left = max(0, (canvas_width - output_width) // 2)
            top = max(0, (canvas_height - output_height) // 2)
            for y, row in enumerate(scaled):
                for x, character in enumerate(row):
                    if character not in (" ", "⠀"):
                        canvas[top + y][left + x] = character

            print("\n".join("".join(row).rstrip() for row in canvas))

    def InitalizeBackground():
        shades = " ░▒▓█"
        terminal = shutil.get_terminal_size((80, 24))
        width = max(20, min(terminal.columns, 100))
        height = max(8, min(terminal.lines - 2, 34))
        start = time.time()
        frame_count = 60

        try:
            sys.stdout.write("\033[?25l\033[2J\033[38;5;46m")
            for frame in range(frame_count):
                elapsed = time.time() - start
                rows = []
                for row in range(height):
                    y = (row / max(1, height - 1) - 0.5) * 2
                    line = []
                    for column in range(width):
                        x = (column / max(1, width - 1) - 0.5) * 3
                        radius = math.sqrt(x * x + y * y)
                        wave_a = math.sin(math.sqrt((x - 0.7) ** 2 + (y + 0.35) ** 2) * 14 - elapsed * 2)
                        wave_b = math.sin(math.sqrt((x + 0.65) ** 2 + (y - 0.4) ** 2) * 13 - elapsed * 1.7)
                        wave_c = math.sin(radius * 10 - elapsed)
                        value = max(0.0, min(0.9999, (wave_a + wave_b + wave_c) / 6 + 0.5))
                        line.append(shades[int(value * len(shades))])
                    rows.append("".join(line))

                sys.stdout.write("\033\n")
                InitializeLogo(background=rows, max_width=20)
                sys.stdout.write("\033[0m\033[38;5;46m")
                sys.stdout.flush()
                time.sleep(1.0 / 20)
        finally:
            sys.stdout.write("\033[?25h\033[0m\n")
            sys.stdout.flush()


    def InitalizeMenu():
        Menu_list = ["Edit Physical Wallet", "Edit Target Wallet", "Mix It Up"]
        n = 0
        print("\n\n")
        for l in Menu_list:
            n += 1
            print(Fore.GREEN + str([n]) + " " + l)

        choice = int(input("\n\nSelect An Option > "))
        if choice == 1:
            os.sys("clear")
            InitalizeBackground()
            cprint("Enter Your Physical Wallet Seed Phrase", "y", True)

            
            seed_words = [] # Collect all seed phrase into a list
            for i in range(1, 13):  # Changes 1-12 automatically
                word = cprintinput(f"{i}: ", "y", False)
                seed_words.append(word)

            CryptoWallets.EditPhysicalWallet(*seed_words)

        elif choice == 2:
            os.sys("clear")
            InitalizeBackground()
            w = cprintinput("Enter Your Target Wallet Address: ", "y", True)
            CryptoWallets.EditTargetWallet(w)

        elif choice == 3:
            os.sys("clear")
            InitalizeBackground()
            CoinMixer.CoinMixer()
            
        else:
            print("Incorrect Option, Please Select a Valid Option.")
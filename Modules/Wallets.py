import os
from Print import *
class CryptoWallets:
    def EditPhysicalWallet(wallet):
        path = "data/Physical Wallet.txt"

        dir_path = os.path.dirname(path) # Get the folder part "data"

        if dir_path and not os.path.exists(dir_path): # Create the folder if it doesn't exist
            os.makedirs(dir_path) # Created the folder

        with open(path, 'w') as f:
            f.write(wallet) # write the wallet data
            printc(f"Successfully Changed Physical Wallet Crypto Address To -> {wallet} !", "g", True)
        
        
    def EditTargetWallet(wallet):
        path = "data/Target Wallet.txt"

        dir_path = os.path.dirname(path) # Get the folder part "data"

        if dir_path and not os.path.exists(dir_path): # Create the folder if it doesn't exist
            os.makedirs(dir_path) # Created the folder

        with open(path, 'w') as f:
            f.write(wallet) # write the wallet data
            printc(f"Successfully Changed Target Wallet Crypto Address To -> {wallet} !", "g", True)


    def RetriveTargetWallet():
        path = "data/Physical Wallet.txt"

        try:
            with open(path, 'r', encoding='utf-8') as file:
                PhysicalWallet = file.read()
            
            return PhysicalWallet

        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
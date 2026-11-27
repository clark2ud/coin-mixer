import os
from Print import *
class CryptoWallets:
    def EditPhysicalWallet(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12):
        path = "data/Physical Wallet.txt"

        dir_path = os.path.dirname(path) # Get the folder part "data"

        if dir_path and not os.path.exists(dir_path): # Create the folder if it doesn't exist
            os.makedirs(dir_path) # Create the folder

    with open(path, 'w') as f:

        f.write("")  # clear the file
    
    # Write each seed  as a new line
    for item in [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]:
        f.write(str(item) + '\n')

    printc(f"Successfully Changed Physical Wallet Crypto Address To -> {s1}, {s2}... !", "g", True)
        
        
    def EditTargetWallet(wallet):
        path = "data/Target Wallet.txt"

        dir_path = os.path.dirname(path) # Get the folder part "data"

        if dir_path and not os.path.exists(dir_path): # Create the folder if it doesn't exist
            os.makedirs(dir_path) # Created the folder

        with open(path, 'w') as f:
            f.write(wallet) # write the wallet data
            printc(f"Successfully Changed Target Wallet Crypto Address To -> {wallet} !", "g", True)


    def RetrivePhysicalWallet():
        path = "data/Physical Wallet.txt"



        try:
            with open(path, 'r', encoding='utf-8') as file:
                PhysicalWallet = file.read() # read the path file
            
            return PhysicalWallet # retrive the wallet

        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
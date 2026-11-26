from colorama import Fore, Back, Style
class Print:
    def cprint(txt, m, is_slow_type=False):
        if m == "g":
            if is_slow_type:
                for character in txt:
                    sys.stdout.write(Fore.GREEN + "[+] " + character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            else:
                if not is_slow_type:
                    print(Fore.GREEN + "[+] " + txt)

        elif m == "r":
            if is_slow_type:
                for character in txt:
                    sys.stdout.write(Fore.RED + "[-] " + character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            else:
                if not is_slow_type:
                    print(Fore.RED + "[-] " + txt)

        elif m == "y":
            if is_slow_type:
                for character in txt:
                    sys.stdout.write(Fore.YELLOW + "[!] " + character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            else:
                if not is_slow_type:
                    print(Fore.YELLOW + "[!] " + txt)

        elif m == "n":
            if is_slow_type:
                for character in txt:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            else:
                if not is_slow_type:
                    print(txt)

    def cprintinput(txt, m, is_slow_type=False):
            inp = ""
            if m == "g":
                if is_slow_type:
                    for character in txt:
                        sys.stdout.write(Fore.GREEN + "[>] " + character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                else:
                    if not is_slow_type:
                        inp = input(Fore.GREEN + "[>] " + txt)
    
            elif m == "r":
                if is_slow_type:
                    for character in txt:
                        sys.stdout.write(Fore.RED + "[>] " + character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                else:
                    if not is_slow_type:
                        inp = input(Fore.RED + "[>] " + txt)
    
            elif m == "y":
                if is_slow_type:
                    for character in txt:
                        sys.stdout.write(Fore.YELLOW + "[>] " + character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                else:
                    if not is_slow_type:
                        inp = input(Fore.YELLOW + "[>] " + txt)
    
            elif m == "n":
                if is_slow_type:
                    for character in txt:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                else:
                    if not is_slow_type:
                        inp = input(txt)

            return inp
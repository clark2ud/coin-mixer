from Modules.Print import Print
class Requirements:
    def InstallRequirements():
        cprint("Checking for Requirements...", "y", True)
        with open("requirements.txt") as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith("#")] # strip all the pure requirements

        for pkg in packages:
            result = subprocess.run([sys.executable, "-m", "pip", "show", pkg], capture_output=True, text=True)
            if result.returncode != 0: # check if the requirements are met
                cprint("Installing Requirements...", "y", True) # install the requirements
                sys.os("python -m pip install")
                try:
                    
                                subprocess.check_call([
                                    sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
                                ])
                                printc("Successfully installed requirements!", "g", True)
                except subprocess.CalledProcessError as e:
                        print(f"Error installing requirements: {e}")
                        raise
            else:
                cprint("Requirements Met.", "g", False) # the requirements were met
                
                return

             
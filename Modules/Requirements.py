from Modules.Print import Print
class Requirements:
    def InstallRequirements():
        cprint("Checking for Requirements...", "y", True)
        with open("requirements.txt") as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

        for pkg in packages:
            result = subprocess.run([sys.executable, "-m", "pip", "show", pkg], capture_output=True, text=True)
            if result.returncode != 0:
                cprint("Installing Requirements...", "y", True)
                
            else:
                cprint("Requirements Met.", "g", True)
                return
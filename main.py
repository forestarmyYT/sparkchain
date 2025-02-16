import json
import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Properly boxed and bold banner
BANNER = f"""
{Style.BRIGHT + Fore.YELLOW}{"*" * 50}
{Style.BRIGHT + Fore.YELLOW}*{" " * 16}𝐅 𝐎 𝐑 𝐄 𝐒 𝐓 𝐀 𝐑 𝐌 𝐘{" " * 16}*
{Style.BRIGHT + Fore.YELLOW}*{" " * 48}*
{Style.BRIGHT + Fore.YELLOW}* {Fore.CYAN}Join us on Telegram: https://t.me/forestarmy {" " * 2}*
{Style.BRIGHT + Fore.YELLOW}{"*" * 50}
"""

def setup_accounts():
    """Set up user accounts and save them to accounts.json."""
    print(f"\n{Style.BRIGHT + Fore.YELLOW}ACCOUNT SETUP")
    num_accounts = int(input(f"\n{Style.BRIGHT + Fore.CYAN}How many accounts do you want to add? {Fore.WHITE}"))

    accounts = []
    for i in range(num_accounts):
        print(f"\n{Style.BRIGHT + Fore.GREEN}Enter details for Account {i+1}:")
        email = input(f"{Style.BRIGHT + Fore.CYAN}Email: {Fore.WHITE}").strip()
        password = input(f"{Style.BRIGHT + Fore.CYAN}Password: {Fore.WHITE}").strip()
        accounts.append({"Email": email, "Password": password})

    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)

    print(f"\n{Style.BRIGHT + Fore.GREEN}✅ Accounts saved successfully in accounts.json!\n")

def run_script():
    """Run bot.py script."""
    print(f"\n{Style.BRIGHT + Fore.YELLOW}RUNNING SCRIPT")
    if os.path.exists("bot.py"):
        print(f"\n{Style.BRIGHT + Fore.GREEN}▶ Running bot.py...\n")
        subprocess.run(["python", "bot.py"])
    else:
        print(f"\n{Style.BRIGHT + Fore.RED}❌ Error: bot.py not found!\n")

def main():
    """Main menu for SPARKCHAIN"""
    print(BANNER)
    print(f"{Style.BRIGHT + Fore.CYAN}1. Account Setup")
    print(f"{Style.BRIGHT + Fore.GREEN}2. Run Script")
    
    choice = input(f"\n{Style.BRIGHT + Fore.YELLOW}Enter your choice (1 or 2): {Fore.WHITE}").strip()
    
    if choice == "1":
        setup_accounts()
    elif choice == "2":
        run_script()
    else:
        print(f"{Style.BRIGHT + Fore.RED}❌ Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
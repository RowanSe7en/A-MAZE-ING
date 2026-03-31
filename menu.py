from algorithm.theme_palette import *

import sys

GOLD = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"
BOLD = "\033[1m"

def menu():
    print(f"\n{GOLD}╔═══════════════════════════════════════╗{RESET}")
    print(f"{GOLD}║{RESET}  {BOLD}{CYAN}🧩  A-MAZE-ING EXPLORER  🧩{RESET}      {GOLD}    ║{RESET}")
    print(f"{GOLD}╠═══════════════════════════════════════╣{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}1 -{RESET} 🔄 Re-generate a new maze    {GOLD}    ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}2 -{RESET} 📍 Show/hide path from entry {GOLD}    ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}3 -{RESET} 🎨 Rotate maze color         {GOLD}    ║{RESET}")
    print(f"{GOLD}║{RESET}  {RED}4 -{RESET} 🚪 Quit                      {GOLD}    ║{RESET}")
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")
    
    choise = input(f"{BOLD}{MAGENTA}Choise? (1-4): {RESET}")
    return choise


def color_menu():
    print(f"\n{GOLD}╔═══════════════════════════════════════╗{RESET}")
    print(f"{GOLD}║{RESET}  {BOLD}{CYAN}🎨  SELECT THEME REALM  🎨{RESET}       {GOLD}    ║{RESET}")
    print(f"{GOLD}╠═══════════════════════════════════════╣{RESET}")
    print(f"{GOLD}║{RESET}  {RED}1 - Lava Theme{RESET}                 {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}2 - Forest Theme{RESET}               {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {CYAN}3 - Ice theme{RESET}                  {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {MAGENTA}4 - Neon theme{RESET}                 {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {GOLD}5 - Sunset theme{RESET}               {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {BOLD}{GREEN}6 - Matrix theme{RESET}               {GOLD}      ║{RESET}")
    print(f"{GOLD}║{RESET}  {BOLD}{CYAN}7 - Party mode{RESET}                 {GOLD}      ║{RESET}")
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")
    
    n = input(f"{BOLD}{MAGENTA}Chose Theme: {RESET} ")
    return n

GOLD = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"
BOLD = "\033[1m"


def menu():

    """Display the main menu and get user's choice."""
    print(f"\n{GOLD}╔═══════════════════════════════════════╗{RESET}")
    print(
        f"{GOLD}║{RESET}  {BOLD}{CYAN}🧩  A-MAZE-ING EXPLORER  🧩{RESET} "
        f"   {GOLD}      ║{RESET}"
    )
    print(f"{GOLD}╠═══════════════════════════════════════╣{RESET}")
    print(
        f"{GOLD}║{RESET}  {GREEN}1 -{RESET} 🔄 Re-generate a new maze   "
        "  "
        f"{GOLD}   ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {GREEN}2 -{RESET} 📍 Show/hide path from entry  "
        f"{GOLD}   ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {GREEN}3 -{RESET} 🎨 Rotate maze color        "
        f"{GOLD}     ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {RED}4 -{RESET} 🚪 Quit                     "
        f"{GOLD}     ║{RESET}"
    )
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")

    choice = input(f"{BOLD}{MAGENTA}Choice? (1-4): {RESET}")
    return choice


def color_menu():
    """Display the theme menu and get user's theme choice."""
    print(f"\n{GOLD}╔═══════════════════════════════════════╗{RESET}")
    print(
        f"{GOLD}║{RESET}  {BOLD}{CYAN}🎨  SELECT THEME REALM  🎨{RESET} "
        f"   {GOLD}       ║{RESET}"
    )
    print(f"{GOLD}╠═══════════════════════════════════════╣{RESET}")
    print(
        f"{GOLD}║{RESET}  {RED}1 - Lava Theme{RESET}                "
        f"{GOLD}       ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {GREEN}2 - Forest Theme{RESET}              "
        f"{GOLD}       ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {CYAN}3 - Ice Theme{RESET}                 "
        f"{GOLD}       ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {MAGENTA}4 - Neon Theme{RESET}               "
        f"{GOLD}        ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {GOLD}5 - Sunset Theme{RESET}              "
        f"{GOLD}       ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {BOLD}{GREEN}6 - Matrix Theme{RESET}            "
        f"{GOLD}         ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {BOLD}{CYAN}7 - Party Mode{RESET}              "
        f"{GOLD}         ║{RESET}"
    )
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")

    theme_choice = input(f"{BOLD}{MAGENTA}Choose Theme: {RESET}")
    return theme_choice

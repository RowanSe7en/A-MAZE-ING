from typing import Dict, Optional

GOLD = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"
BOLD = "\033[1m"


def menu() -> str:

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
        f"{GOLD}║{RESET}  {GREEN}4 -{RESET} 🛠️  Change Config            "
        f"{GOLD}     ║{RESET}"
    )
    print(
        f"{GOLD}║{RESET}  {RED}5 -{RESET} 🚪 Quit                     "
        f"{GOLD}     ║{RESET}"
    )
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")

    choice: str = input(f"{BOLD}{MAGENTA}Choice? (1-4): {RESET}")
    return choice


def color_menu() -> str:
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
        f"{GOLD}║{RESET}  {BOLD}{CYAN}7 - Random Theme{RESET}            "
        f"{GOLD}         ║{RESET}"
    )
    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")

    theme_choice: str = input(f"{BOLD}{MAGENTA}Choose Theme: {RESET}")
    try:
        int_theme = int(theme_choice)
        if int_theme < 1 or int_theme > 7:
            print("Invalid choice, choose again.")
            return color_menu()
    except ValueError:
        print("Invalid choice, choose again.")
        return color_menu()
    return theme_choice


def change_config() -> Dict[str, Optional[str]]:
    """Display config menu and change a configuration value."""
    all_keys = [
        "width", "height", "entry", "exit",
        "seed", "perfect", "generate_time", "solve_time"
    ]

    print(f"\n{GOLD}╔═══════════════════════════════════════╗{RESET}")
    print(
        f"{GOLD}║{RESET}   {BOLD}{CYAN}⚙️  CHANGE CONFIGURATION  ⚙️{RESET} "
        f"{GOLD}         ║{RESET}"
    )
    print(f"{GOLD}╠═══════════════════════════════════════╣{RESET}")

    print(f"{GOLD}║{RESET}  {GREEN}1 - Width{RESET}  (ex: 30)          "
          f"{GOLD}        ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}2 - Height{RESET} (ex: 15)         "
          f"{GOLD}         ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}3 - Entry{RESET}  (ex: 0,0)        "
          f"{GOLD}         ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}4 - Exit{RESET}   (ex: 29,14)      "
          f"{GOLD}         ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}5 - Seed{RESET}   (ex: 42)         "
          f"{GOLD}         ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}6 - Perfect Maze{RESET} (true/false)"
          f"{GOLD}        ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}7 - Generate Time{RESET} (#.##)"
          f"{GOLD}             ║{RESET}")
    print(f"{GOLD}║{RESET}  {GREEN}8 - Solve Time{RESET} (#.##) "
          f"{GOLD}               ║{RESET}")
    print(
        f"{GOLD}║{RESET}  {GREEN}9 - Bo back home{RESET}"
        f"{GOLD}        ║{RESET}"
        )

    print(f"{GOLD}╚═══════════════════════════════════════╝{RESET}")

    key_chois: str = input(f"{BOLD}{MAGENTA}Enter Choice: {RESET}")

    if int(key_chois) < len(all_keys) + 1:
        data_key: str = all_keys[int(key_chois) - 1]
        val: str = input(
            f"{BOLD}{CYAN}Enter New Value "
            f"(check example above): {RESET}"
        )
        while val == "":
            print("Invalid choice, choose again.")
            val: str = input(
                f"{BOLD}{CYAN}Enter New Value "
                f"(check example above): {RESET}"
            )

        new_dict = {data_key: val}
    elif int(key_chois) == 9:
        print("Going back home.")
        return {}
    else:
        print("Invalid choice, choose again.")
        change_config()

    return new_dict

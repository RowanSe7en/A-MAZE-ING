import algorithm

class Color:
    reset  = "\033[0m"
    bold   = "\033[1m"
    dim    = "\033[2m"

    red    = "\033[31m"
    green  = "\033[32m"
    yellow = "\033[33m"
    blue   = "\033[34m"
    magenta= "\033[35m"
    cyan   = "\033[36m"
    white  = "\033[37m"


def ascii_landing():

    algorithm.clear()

    print(f"""{Color.cyan}{Color.dim}
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                  ║
    ║{Color.magenta}{Color.bold}      █████╗     ███╗   ███╗ █████╗ ███████╗███████╗    ██╗███╗   ██╗ ██████╗     {Color.cyan}{Color.dim}║
    ║{Color.magenta}{Color.bold}     ██╔══██╗    ████╗ ████║██╔══██╗╚══███╔╝██╔════╝    ██║████╗  ██║██╔════╝     {Color.cyan}{Color.dim}║
    ║{Color.magenta}{Color.bold}     ███████║    ██╔████╔██║███████║  ███╔╝ █████╗      ██║██╔██╗ ██║██║  ███╗    {Color.cyan}{Color.dim}║
    ║{Color.magenta}{Color.bold}     ██╔══██║    ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝      ██║██║╚██╗██║██║   ██║    {Color.cyan}{Color.dim}║
    ║{Color.magenta}{Color.bold}     ██║  ██║    ██║ ╚═╝ ██║██║  ██║███████╗███████╗    ██║██║ ╚████║╚██████╔╝    {Color.cyan}{Color.dim}║
    ║{Color.magenta}{Color.bold}     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚═════╝     {Color.cyan}{Color.dim}║
    ║                                                                                  ║
    ║{Color.yellow}{Color.bold}                           🧩  A - M A Z E - I N G  🧩                            {Color.cyan}{Color.dim}║
    ║                                                                                  ║
    ║{Color.white}                         Created by brouane / bmarbouh                            {Color.cyan}{Color.dim}║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║                                                                                  ║
    ║{Color.green}   ● Generate perfect & imperfect mazes                                           {Color.cyan}{Color.dim}║
    ║{Color.green}   ● Visualize solving algorithms                                                 {Color.cyan}{Color.dim}║
    ║{Color.green}   ● Optional colored rendering                                                   {Color.cyan}{Color.dim}║
    ║                                                                                  ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    {Color.reset}""")

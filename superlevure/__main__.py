import sys


def print_c(string, message_type="info", endline=True, tqdm_=False):
    """
        print_colored
        """
    COMMANDS = {
        "info": (33, "[!] "),
        "que": (34, "[?] "),
        "bad": (31, "[-] "),
        "good": (32, "[+] "),
        "run": (97, "[~] "),
    }
    message = "\033[{}m{}\033[0m{}".format(
        COMMANDS[message_type][0], COMMANDS[message_type][1], string
    )

    if not tqdm_:
        print(message, end=("\n" if endline else ""))
    else:
        if "tqdm" in sys.modules:
            tqdm.write(message)

import sys
import json


def init_conf_file(name="conf.json"):

    conf = open(name, "r")
    conf = json.load(conf)

    return conf


class ColoredPrint:
    def __init__(self):
        self.telegram = None

    def telegram_connect(self, telegram):
        self.telegram = telegram

    def print_c(self, string, message_type="info", endline=True, tqdm_=False):
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

        if self.telegram:
            pass


print_c = ColoredPrint().print_c
